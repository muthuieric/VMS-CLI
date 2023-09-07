# cli.py
import click
from db import init_db, Session

@click.command()
def initdb():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@click.command()
@click.option('--visitor', help='Visitor full name')
@click.option('--email', help='Visitor email')
def addvisitor(visitor, email):
    """Add a new visitor."""
    session = Session()
    new_visitor = Visitor(full_name=visitor, email=email)
    session.add(new_visitor)
    session.commit()
    click.echo(f'Visitor {visitor} added successfully.')

# Define more Click commands for managing offices and visits

if __name__ == '__main__':
    initdb()
    addvisitor()
