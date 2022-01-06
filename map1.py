import folium
import pandas

# read Volcanoes.txt
data = pandas.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


# function to produce the marker's color depending on the elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


# create map instance with specific parameters
map = folium.Map(location=[33.378, -118.426],
                 zoom_start=6, tiles='Stamen Terrain')

# add features to the map
fg = folium.FeatureGroup(name='My Map')

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(
        html=f'Volcano name: <a href="https://www.google.com/search?q={name}" target="_blank">{name}</a><br>Height: {el} ft', width=200, height=100)
    # fg.add_child(folium.Marker(
    #     location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
    fg.add_child(folium.CircleMarker(radius=10,
                                     location=[lt, ln], popup=folium.Popup(iframe), color='grey', fill_color=color_producer(el), fill_opacity=0.7))

# add feature group to the map
map.add_child(fg)

# generate the map as html doc
map.save('Map1.html')
