import folium
import pandas

data = pandas.read_csv("D:\Python_Learning\Application_2_web_Map\Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])
#name = list(data["NAME"])

#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""

def color_producers(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2500:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[38.58,-99.09],zoom_start =6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, el in zip(lat,lon,elv):
#for cordinates in [[38.58,-99.09],[36.58,-98.09]]:
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"  meters", icon=folium.Icon(color=color_producers(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"  meters",fill_color =color_producers(el),color='grey',fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x ['properties']['POP2005']< 10000000
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")