import folium

# create map instance with specific parameters
map = folium.Map(location=[33.378, -118.426],
                 zoom_start=8, tiles='Stamen Terrain')

# add features to the map
fg = folium.FeatureGroup(name='My Map')

for coordinates in [[33.378, -118.426], [33.478, -119.426]]:
    fg.add_child(folium.Marker(
        location=coordinates, popup='Catalina', icon=folium.Icon(color='green')))

# add feature group to the map
map.add_child(fg)

# generate the map as html doc
map.save('Map1.html')
