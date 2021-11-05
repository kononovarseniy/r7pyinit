import itertools
import pkgutil
import subprocess
import textwrap
from pathlib import Path

MODULE_INIT_FILE = '__init__.py'
README_FILE = 'README.md'
GITIGNORE_FILE = '.gitignore'

DEV_DEPENDENCIES = (
    # Typing
    'mypy',
    # Formatting
    'autopep8',
    # Refactoring
    'rope'
)

README_TEMPLATE = textwrap.dedent('''\
    # {project_name}
''')


def create_file_structure(root: Path, project_name: str) -> None:
    root.mkdir(parents=True, exist_ok=False)

    root_module_path = root.joinpath(project_name)
    root_module_path.mkdir()

    root_init_path = root_module_path.joinpath(MODULE_INIT_FILE)
    root_init_path.touch()

    readme_path = root.joinpath(README_FILE)
    readme_path.write_text(README_TEMPLATE.format(project_name=project_name))

    import r7pyinit
    gitignore_content = pkgutil.get_data(r7pyinit.__name__, 'resources/gitignore')
    assert gitignore_content is not None
    gitignore_path = root.joinpath(GITIGNORE_FILE)
    gitignore_path.write_bytes(gitignore_content)


def init_poetry(root: Path, project_name: str) -> None:
    base_command = 'poetry', 'init', '-n'
    name_arg = '--name', project_name
    dev_dependencies_args = itertools.chain.from_iterable(
        ['--dev-dependency', d] for d in DEV_DEPENDENCIES)
    command = list(itertools.chain(base_command, name_arg, dev_dependencies_args))
    subprocess.run(command, cwd=root)
    subprocess.run('poetry config --local virtualenvs.in-project true', shell=True, cwd=root)
    subprocess.run('poetry install', shell=True, cwd=root)


def init_repo(root: Path) -> None:
    subprocess.run('git init', shell=True, cwd=root)
    subprocess.run('git add .', shell=True, cwd=root)


def create_project(root: Path, project_name: str) -> None:
    create_file_structure(root, project_name)
    init_poetry(root, project_name)
    init_repo(root)
