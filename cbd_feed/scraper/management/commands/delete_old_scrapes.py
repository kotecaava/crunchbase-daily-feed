import pytz
from datetime import (
    datetime,
    timedelta,
)
from django.core.management.base import BaseCommand

from scraper.models import Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Deleting old scrapes...')
        today = datetime.now(pytz.utc)
        year_ago = today - timedelta(days=365)
        old_scrapes = Result.objects.filter(created_at__lt=year_ago)
        num_deleted = old_scrapes.delete()[0];

        print('Deleted {} old scrapes'.format(num_deleted))
