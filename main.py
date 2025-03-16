import folium
import requests
import pandas

if __name__ == "__main__":
    state_geo = requests.get(
        "https://raw.githubusercontent.com/PhantByte/PhantMaps/refs/heads/main/data/geometry.json"
    ).json()
    state_data = pandas.read_csv(
        "https://raw.githubusercontent.com/PhantByte/PhantMaps/refs/heads/main/data/rates.csv"
    ) #acum tre sa folosim data-ul nostru

    m = folium.Map(location=(50, 10), tiles="cartodb positron", zoom_start=4)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["CountryCode", "2023"],
        key_on="feature.id",
        fill_color="RdYlGn", # de aici putem schimba gradientul
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Gradul de urbanizare (%)",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    m.save("index.html")
