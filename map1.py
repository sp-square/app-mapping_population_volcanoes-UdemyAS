import folium
import pandas

# read Volcanoes.txt
data = pandas.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# create map instance with specific parameters
map = folium.Map(location=[33.378, -118.426],
                 zoom_start=8, tiles='Stamen Terrain')

# add features to the map
fg = folium.FeatureGroup(name='My Map')

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(
        html=f'Volcano name: <a href="https://www.google.com/search?q={name}" target="_blank">{name}</a><br>Height: {el} ft', width=200, height=100)
    fg.add_child(folium.Marker(
        location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

# add feature group to the map
map.add_child(fg)

# generate the map as html doc
map.save('Map1.html')
