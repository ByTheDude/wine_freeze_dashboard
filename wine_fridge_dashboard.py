import streamlit as st

# Define fridge layout
shelf_layout = {
    1: {'type': 'flat', 'capacity': 8},
    2: {'type': 'pile', 'capacity': 15},
    3: {'type': 'flat', 'capacity': 10},
    4: {'type': 'flat', 'capacity': 10},
    5: {'type': 'flat', 'capacity': 10},
    6: {'type': 'flat', 'capacity': 10},
    7: {'type': 'flat', 'capacity': 10},
    8: {'type': 'flat', 'capacity': 10},
    9: {'type': 'flat', 'capacity': 10},
}

# Example wines in specific locations
mock_wines = [
    ("Chateau Margaux 2015", 1, 1),
    ("Opus One 2018", 1, 2),
    ("Penfolds Grange 2014", 1, 3),
    ("Sassicaia 2019", 2, 1),
    ("Sassicaia 2019", 2, 2),
    ("Sassicaia 2019", 2, 3),
    ("Tignanello 2016", 3, 1),
    ("Tignanello 2016", 3, 2),
    ("Barolo Monfortino 2013", 3, 3),
    ("Dominus 2015", 3, 4),
]

st.set_page_config(layout="wide")
st.title("Wine Fridge Visualizer")
st.markdown("Visual layout of your 9-shelf wine fridge.")

# Render each shelf
for shelf in range(1, 10):
    layout = shelf_layout[shelf]
    st.markdown(f"### Shelf {shelf} ({layout['type']})")
    cols = st.columns(layout['capacity'])

    for i in range(layout['capacity']):
        wine = next((w[0] for w in mock_wines if w[1] == shelf and w[2] == i + 1), "")
        with cols[i]:
            st.button(wine if wine else "[Empty Slot]", key=f"{shelf}-{i+1}")
