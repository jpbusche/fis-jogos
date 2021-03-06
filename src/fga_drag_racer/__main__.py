import argparse
import fga_drag_racer
import os
from fga_drag_racer import __version__


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('FGA Drag Racer')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser

def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # Put your main script logic here
    path = os.path.dirname(__file__)
    os.chdir(path)
    os.system('pgzrun main.py')


if __name__ == '__main__':
    main()