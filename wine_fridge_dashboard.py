import streamlit as st import streamlit.components.v1 as components

Define fridge layout

shelf_layout = { 1: {'type': 'flat', 'capacity': 8}, 2: {'type': 'pile', 'capacity': 15}, 3: {'type': 'flat', 'capacity': 10}, 4: {'type': 'flat', 'capacity': 10}, 5: {'type': 'flat', 'capacity': 10}, 6: {'type': 'flat', 'capacity': 10}, 7: {'type': 'flat', 'capacity': 10}, 8: {'type': 'flat', 'capacity': 10}, 9: {'type': 'flat', 'capacity': 10}, }

Example wines in specific locations

mock_wines = [ ("Chateau Margaux 2015", 1, 1, "France", "Drink by 2035"), ("Opus One 2018", 1, 2, "USA", "Drink by 2032"), ("Penfolds Grange 2014", 1, 3, "Australia", "Drink by 2040"), ("Sassicaia 2019", 2, 1, "Italy", "Drink by 2030"), ("Sassicaia 2019", 2, 2, "Italy", "Drink by 2030"), ("Sassicaia 2019", 2, 3, "Italy", "Drink by 2030"), ("Tignanello 2016", 3, 1, "Italy", "Drink by 2029"), ("Tignanello 2016", 3, 2, "Italy", "Drink by 2029"), ("Barolo Monfortino 2013", 3, 3, "Italy", "Drink by 2040"), ("Dominus 2015", 3, 4, "USA", "Drink by 2035"), ]

st.set_page_config(layout="wide") st.markdown(""" <style> .wine-button { background-color: #f0f8ff; border-radius: 10px; padding: 10px; font-weight: bold; border: 2px solid #4682B4; margin: 2px; text-align: center; width: 100%; } .empty-button { background-color: #eee; border-radius: 10px; padding: 10px; border: 1px dashed #bbb; margin: 2px; text-align: center; width: 100%; } </style> """, unsafe_allow_html=True)

st.title("Wine Fridge Visualizer") st.markdown("Explore your 9-shelf wine fridge visually. Hover over a bottle to see details.")

Render each shelf

for shelf in range(1, 10): layout = shelf_layout[shelf] st.markdown(f"#### Shelf {shelf} ({layout['type'].capitalize()})") cols = st.columns(layout['capacity'])

for i in range(layout['capacity']):
    wine_data = next((w for w in mock_wines if w[1] == shelf and w[2] == i + 1), None)
    with cols[i]:
        if wine_data:
            name, _, _, region, notes = wine_data
            tooltip = f"{name} ({region})<br>{notes}"
            components.html(f'<div class="wine-button" title="{tooltip}">{name}</div>', height=50)
        else:
            components.html('<div class="empty-button">Empty</div>', height=50)

