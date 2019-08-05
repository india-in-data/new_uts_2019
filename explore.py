import geopandas
import geojsonio
import json
import sys

shape = geopandas.read_file(sys.argv[1])

ladakh = shape[(shape['district'] == 'Leh (ladakh)') | (shape['district'] == 'Kargil')]
ladakh.to_file(sys.argv[2], driver='GeoJSON')