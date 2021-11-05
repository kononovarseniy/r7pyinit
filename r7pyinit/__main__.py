import argparse
from pathlib import Path

from r7pyinit.create_project import create_project

PROGRAM = 'r7pyinit'
DESCRIPTION = 'Create basic python project. Initializes git and poetry for development using vscode.'

parser = argparse.ArgumentParser(prog=PROGRAM, description=DESCRIPTION, )
parser.add_argument('project_name', type=str, help='Name of the project.')
parser.add_argument('--path', type=Path, help='Root path of the project.')

args = parser.parse_args()

project_name: str = args.project_name
root_path: Path = args.path or Path(args.project_name)

create_project(root_path, project_name)
