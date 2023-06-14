from pathlib import Path
import json
import click

@click.command()
def open_input_file():
    click.open_file(Path(__file__).parent / "In")
@click.command()
def write_to_output_folder():
    click.echo('', Path(__file__).parent / "Out")

# @click.command()
# def make_json():
#     click.

@click.command()
def hello():
    click.echo('Hello World!')

#Main
#if __name__ == '__main__':
#output_folder = get_output_path()

hello()
