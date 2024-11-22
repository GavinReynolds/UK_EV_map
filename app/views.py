from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from .models import EVChargingLocations

# Create your views here.
def home(request):
    sites = EVChargingLocations.objects.all()[:5000]
    # initialise map
    m = folium.Map(location=[51.5812,0.1837], zoom_start=10)
    
    latitude = [site.latitude for site in sites]
    longitude = [site.longitude for site in sites]

    FastMarkerCluster(data=list(zip(latitude, longitude))).add_to(m)

    context = {'map': m._repr_html_()}
    return render(request, 'home.html', context)