import argparse
from pathlib import Path

from r7pyinit.create_project import create_project

PROGRAM = 'r7pyinit'
DESCRIPTION = 'Create basic python project. Initializes git and poetry for development using vscode.'

parser = argparse.ArgumentParser(prog=PROGRAM, description=DESCRIPTION, )
parser.add_argument('path', type=Path, help='Root path of the project.')
parser.add_argument('project_name', type=str, help='Name of the project.')

args = parser.parse_args()

create_project(args.path, args.project_name)
