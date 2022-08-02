"""
Django command to wait for database to be avaiable.
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand # noqa


class Command(BaseCommand):
    """Django command to wait database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavaiable, waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
