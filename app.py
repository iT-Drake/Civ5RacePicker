import streamlit as st

from random import choice
from os import path
from json import load

def load_data(file_name):
    if not path.exists(file_name):
        return []
    
    with open(file_name, 'r', encoding='utf-8') as file:
        return load(file)

LOCALIZATION_FILE = 'data/localization.json'
CIVILIZATIONS_FILE = 'data/civilizations.json'
LOCALIZATION = load_data(LOCALIZATION_FILE)

def error(text):
    st.error(text, icon=':material/error:')
    st.stop()

def default_groups():
    group1 = {
        "America": {"Icon": "https://static.wikia.nocookie.net/civilization/images/c/c0/American_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/American_(Civ5)"},
        "Assyria": {"Icon": "https://static.wikia.nocookie.net/civilization/images/c/ca/Assyrian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Assyrian_(Civ5)"},
        "Austria": {"Icon": "https://static.wikia.nocookie.net/civilization/images/9/92/Austrian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Austrian_(Civ5)"},
        "Brazil": {"Icon": "https://static.wikia.nocookie.net/civilization/images/d/d7/Brazilian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Brazilian_(Civ5)"},
        "Byzantium": {"Icon": "https://static.wikia.nocookie.net/civilization/images/8/8c/Byzantine_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Byzantine_(Civ5)"},
        "Celts": {"Icon": "https://static.wikia.nocookie.net/civilization/images/d/d1/Celtic_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Celtic_(Civ5)"},
        "Dutch": {"Icon": "https://static.wikia.nocookie.net/civilization/images/6/60/Dutch_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Dutch_(Civ5)"},
        "France": {"Icon": "https://static.wikia.nocookie.net/civilization/images/5/5e/French_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/French_(Civ5)"},
        "Indonesia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/f/f2/Indonesian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Indonesian_(Civ5)"},
        "Polynesia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/2/28/Polynesian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Polynesian_(Civ5)"},
        "Portugal": {"Icon": "https://static.wikia.nocookie.net/civilization/images/1/11/Portuguese_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Portuguese_(Civ5)"},
        "Siam": {"Icon": "https://static.wikia.nocookie.net/civilization/images/5/5b/Siamese_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Siamese_(Civ5)"},
        "Spain": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/e9/Spanish_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Spanish_(Civ5)"},
        "Sweden": {"Icon": "https://static.wikia.nocookie.net/civilization/images/2/27/Swedish_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Swedish_(Civ5)"},
        "Venice": {"Icon": "https://static.wikia.nocookie.net/civilization/images/5/52/Venetian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Venetian_(Civ5)"}
    }

    group2 = {
        "Carthage": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/e3/Carthaginian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Carthaginian_(Civ5)"},
        "China": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/e8/Chinese_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Chinese_(Civ5)"},
        "Denmark": {"Icon": "https://static.wikia.nocookie.net/civilization/images/6/61/Danish_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Danish_(Civ5)"},
        "England": {"Icon": "https://static.wikia.nocookie.net/civilization/images/1/1c/English_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/English_(Civ5)"},
        "Germany": {"Icon": "https://static.wikia.nocookie.net/civilization/images/d/d5/German_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/German_(Civ5)"},
        "Huns": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/ee/Hunnic_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Hunnic_(Civ5)"},
        "Iroquois": {"Icon": "https://static.wikia.nocookie.net/civilization/images/b/b6/Iroquois_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Iroquois_(Civ5)"},
        "Japan": {"Icon": "https://static.wikia.nocookie.net/civilization/images/7/7c/Japanese_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Japanese_(Civ5)"},
        "Mongolia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/4/42/Mongolian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Mongolian_(Civ5)"},
        "Ottomans": {"Icon": "https://static.wikia.nocookie.net/civilization/images/c/c2/Ottoman_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Ottoman_(Civ5)"},
        "Rome": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/ea/Roman_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Roman_(Civ5)"},
        "Shoshone": {"Icon": "https://static.wikia.nocookie.net/civilization/images/a/ab/Shoshone_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Shoshone_(Civ5)"},
        "Songhai": {"Icon": "https://static.wikia.nocookie.net/civilization/images/f/f9/Songhai_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Songhai_(Civ5)"},
        "Zulus": {"Icon": "https://static.wikia.nocookie.net/civilization/images/e/e9/Zulu_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Zulu_(Civ5)"}
    }

    group3 = {
        "Arabia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/8/81/Arabian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Arabian_(Civ5)"},
        "Aztec": {"Icon": "https://static.wikia.nocookie.net/civilization/images/8/89/Aztec_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Aztec_(Civ5)"},
        "Babylon": {"Icon": "https://static.wikia.nocookie.net/civilization/images/3/33/Babylonian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Babylonian_(Civ5)"},
        "Egypt": {"Icon": "https://static.wikia.nocookie.net/civilization/images/1/1a/Egyptian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Egyptian_(Civ5)"},
        "Ethiopia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/9/92/Ethiopian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Ethiopian_(Civ5)"},
        "Greece": {"Icon": "https://static.wikia.nocookie.net/civilization/images/5/56/Greek_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Greek_(Civ5)"},
        "Inca": {"Icon": "https://static.wikia.nocookie.net/civilization/images/7/77/Incan_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Incan_(Civ5)"},
        "India": {"Icon": "https://static.wikia.nocookie.net/civilization/images/5/5e/Indian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Indian_(Civ5)"},
        "Korea": {"Icon": "https://static.wikia.nocookie.net/civilization/images/7/76/Korean_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Korean_(Civ5)"},
        "Maya": {"Icon": "https://static.wikia.nocookie.net/civilization/images/4/48/Mayan_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Mayan_(Civ5)"},
        "Morocco": {"Icon": "https://static.wikia.nocookie.net/civilization/images/a/ad/Moroccan_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Moroccan_(Civ5)"},
        "Persia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/2/28/Persian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Persian_(Civ5)"},
        "Poland": {"Icon": "https://static.wikia.nocookie.net/civilization/images/3/31/Polish_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Polish_(Civ5)"},
        "Russia": {"Icon": "https://static.wikia.nocookie.net/civilization/images/c/c5/Russian_%28Civ5%29.png", "Link": "https://civilization.fandom.com/wiki/Russian_(Civ5)"}
    }

    return [group1, group2, group3]

def civilization_list(groups):
    civ_list = []
    for group in groups:
        civ_list += list(group.keys())

    return sorted(civ_list)

def civilization_link(icon, link, caption):
    content = f"""
        <div class="stImage" data-testid="stImage" style="width: 94px;">
            <div data-testid="stImageContainer">
                <a href='{link}'>
                    <img style="width: 94px; max-width: 100%;" src="{icon}" alt="0">
                </a>
                <div data-testid="stImageCaption" style="width: 94px; max-width: 100%; text-align: center;">
                    <span style='font-size: 24px;'>{caption}<span>
                </div>
            </div>
        </div>
    """
    st.markdown(content, unsafe_allow_html=True)

def player_choices(groups, players, banned):
    for civilization in banned:
        for group in groups:
            if civilization in group:
                group.pop(civilization)
            if len(group) < players:
                error(LOCALIZATION['ErrorNotEnoughItems'])

    result = []
    for _ in range(0, players):
        player_choices = []
        for group in groups:
            civilization = choice(list(group.keys()))
            data = group.pop(civilization)
            player_choices.append({'Civ': civilization, 'Icon': data['Icon'], 'Link': data['Link']})
        result.append(player_choices)

    return result

def display_choices(choices, columns = None):
    if not choices:
        return
    
    if columns == None or len(choices) < columns:
        columns = len(choices)

    collection = st.columns(columns)
    index = 0
    player_index = 1
    for player in choices:
        column = collection[index]

        with column:
            st.subheader(f'{LOCALIZATION["PlayerColumnCaption"]} {player_index}')
            for choice in player:
                civilization_link(choice['Icon'], choice['Link'], choice['Civ'])
            st.divider()

        index += 1
        player_index += 1
        if index >= columns:
            index = 0

def draw_interface():
    st.header(LOCALIZATION['Header'])

    col1, col2 = st.columns(2)

    groups = load_data(CIVILIZATIONS_FILE)
    if not groups:
        groups = default_groups()
    civ_list = civilization_list(groups)

    with col1:
        players = range(1, 9)
        players = st.selectbox('Players', players, index=None, placeholder=LOCALIZATION['PlayersNumberField'], label_visibility='hidden')

    with col2:
        banned = st.multiselect('Banned', civ_list, placeholder=LOCALIZATION['BannedCivilizationsField'], label_visibility='hidden')

    if st.button(LOCALIZATION['GenerateButton'], use_container_width=True):
        if players:
            choices = player_choices(groups, int(players), banned)
            display_choices(choices, 4)

draw_interface()
