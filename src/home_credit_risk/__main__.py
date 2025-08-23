"""Home Credit Default Risk ML project package entry-point."""

from pathlib import Path
import os

from kedro.framework.cli.main import main


def main():
    package_name = Path(__file__).parent.name
    os.chdir(Path(__file__).parent.parent.parent)
    main(["--help"])


if __name__ == "__main__":
    main()