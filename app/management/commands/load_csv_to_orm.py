from django.core.management.base import BaseCommand
import csv
from app.models import EVChargingLocations

class Command(BaseCommand):
    help = 'Load csv data to orm'

    def handle(self, *args, **options):
        csv_data = '../national-charge-point-registry.csv'
        # Open and load csv data in to EVChargingLocations
        with open(csv_data, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                EVChargingLocations.objects.get_or_create(
                    name = row['name'],
                    latitude = row['latitude'],
                    longitude = row['longitude']
                )
