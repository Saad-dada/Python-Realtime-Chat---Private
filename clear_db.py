from website import create_app, db
from website.models import User, Message, Room

app = create_app()

def delete_all_records():
    with app.app_context():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())  # Delete all rows
        db.session.commit()
        print("All records deleted.")

delete_all_records()
