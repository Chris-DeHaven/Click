from pathlib import Path
import json
import click
from traverse_folders import make_json


@click.command()
@click.argument(
    "in_folder",
    type=click.Path(exists=True, file_okay=False),
    default=Path(__file__).parent / "In",
)
@click.argument(
    "out_folder",
    type=click.Path(exists=True, file_okay=False),
    default=Path(__file__).parent / "Out",
)
def main(in_folder, out_folder):
    print("in_folder = ")
    print(in_folder)
    print("out_folder = ")
    print(out_folder)


# Main
if __name__ == "__main__":
    main()
