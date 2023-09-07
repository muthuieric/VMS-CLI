# vms/app/visits.py
import click
from models import Visit, session
from datetime import datetime  # Import datetime for current date and time

@click.group()
def visits():
    """Manage visits."""
    pass

@visits.command()
@click.option('--person-visited', prompt='Enter person visited', help='Person visited')
def add(person_visited):
    """Add a visit."""
    # In the previous steps, visitor_id and office_id should have been stored in variables.
    # Assuming you have visitor_id and office_id available, you can link them here.
    
    # Replace 'visitor_id' and 'office_id' with the actual values you have from previous steps.
    visitor_id = 1  # Replace with the actual visitor_id.
    office_id = 1   # Replace with the actual office_id.

    # Get the current date and time
    current_datetime = datetime.now()

    # Create the visit record
    visit = Visit(visitor_id=visitor_id, office_id=office_id, person_visited=person_visited, visit_date=current_datetime)
    session.add(visit)
    session.commit()
    click.echo("Visit added.")

@visits.command()
def list():
    """List all visits."""
    visits = session.query(Visit).all()
    click.echo("Visits:")
    for visit in visits:
        click.echo(f"ID: {visit.visit_id}, Visitor ID: {visit.visitor_id}, Office ID: {visit.office_id}, Person Visited: {visit.person_visited}, Visit Date: {visit.visit_date}")

@visits.command()
@click.argument('visit_id', type=int)
@click.option('--person-visited', prompt='Enter updated person visited', help='Updated person visited')
def update(visit_id, person_visited):
    """Update a visit by ID."""
    visit = session.query(Visit).filter_by(visit_id=visit_id).first()
    if visit:
        visit.person_visited = person_visited
        session.commit()
        click.echo(f"Visit with ID {visit_id} updated.")
    else:
        click.echo(f"Visit with ID {visit_id} not found.")

@visits.command()
@click.argument('visit_id', type=int)
def delete(visit_id):
    """Delete a visit by ID."""
    visit = session.query(Visit).filter_by(visit_id=visit_id).first()
    if visit:
        session.delete(visit)
        session.commit()
        click.echo(f"Visit with ID {visit_id} deleted.")
    else:
        click.echo(f"Visit with ID {visit_id} not found.")


@visits.command()
@click.argument('visit_id', type=int)
def search(visit_id):
    """Search for a visit by ID using binary search."""
    visits = session.query(Visit).all()
    
    # Binary search to find the visit by ID
    left, right = 0, len(visits) - 1
    while left <= right:
        mid = (left + right) // 2
        if visits[mid].visit_id == visit_id:
            click.echo(f"Visit found - ID: {visits[mid].visit_id}, Visitor ID: {visits[mid].visitor_id}, Office ID: {visits[mid].office_id}")
            return
        elif visits[mid].visit_id < visit_id:
            left = mid + 1
        else:
            right = mid - 1
    
    click.echo(f"Visit with ID {visit_id} not found.")