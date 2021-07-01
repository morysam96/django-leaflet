from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from .models import *


admin.site.register(MushroomSpot, LeafletGeoAdmin)
