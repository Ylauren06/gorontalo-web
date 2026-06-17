import folium

# Pusat peta Provinsi Gorontalo
m = folium.Map(location=[0.54, 123.06], zoom_start=8)

folium.TileLayer(
    tiles='https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}',
    attr='&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.stamen.com/" target="_blank">Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    name='Stamen Watercolor',
).add_to(m)

folium.LayerControl(collapsed=False).add_to(m)

# Marker tiap wilayah
folium.Marker(
    location=[0.6369, 122.2830],
    popup="Boalemo\nPenduduk: 155183 jiwa"
).add_to(m)

folium.Marker(
    location=[0.7016, 122.9773],
    popup="Kabupaten Gorontalo\nPenduduk: 413627 jiwa"
).add_to(m)

folium.Marker(
    location=[0.4498, 121.9385],
    popup="Pohuwato\nPenduduk: 155665 jiwa"
).add_to(m)

folium.Marker(
    location=[0.5545, 123.1474],
    popup="Bone Bolango\nPenduduk: 172726 jiwa"
).add_to(m)

folium.Marker(
    location=[0.8306, 122.8708],
    popup="Gorontalo Utara\nPenduduk: 134852 jiwa"
).add_to(m)

folium.Marker(
    location=[0.5412, 123.0595],
    popup="Kota Gorontalo\nPenduduk: 210185 jiwa"
).add_to(m)

# Menambahkan legenda di kanan bawah
legend_html = '''
<div style="
position: fixed;
bottom: 50px;
right: 50px;
width: 150px;
height: 90px;
background-color: white;
border:2px solid grey;
z-index:9999;
font-size:14px;
padding: 10px;
border-radius: 5px;
">
<b>Legenda</b><br><br>
<span style="color:red;">●</span> Kabupaten
</div>
'''

m.get_root().html.add_child(folium.Element(legend_html))

# Simpan peta
m.save("index.html")