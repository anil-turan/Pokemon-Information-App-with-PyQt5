import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

class PokemonInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Pokemon Info')
        self.setGeometry(100, 100, 500, 300)

        self.label = QLabel('Enter the Pokémon name:')
        self.input_text = QLineEdit()
        self.submit_button = QPushButton('Get Info')
        self.info_label = QLabel('')
        self.pokemon_image = QLabel()  # Label for Pokemon image

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.info_label)
        layout.addWidget(self.pokemon_image)  # Add image label to the layout

        self.submit_button.clicked.connect(self.get_pokemon_info)
        self.setLayout(layout)

    def get_pokemon_info(self):
        pokemon_name = self.input_text.text()
        pokemon_info, pokemon_image_url = self.fetch_pokemon_info(pokemon_name)

        if pokemon_info:
            info_text = f"Name: {pokemon_info['name']}\nHeight: {pokemon_info['height']}\nWeight: {pokemon_info['weight']}\nAbilities: {', '.join(pokemon_info['abilities'])}\nTypes: {', '.join(pokemon_info['types'])}"
            self.info_label.setText(info_text)
            
            if pokemon_image_url:
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(pokemon_image_url).content)
                pixmap = pixmap.scaled(self.pokemon_image.size(), aspectRatioMode=True)
                self.pokemon_image.setPixmap(pixmap)
        else:
            self.info_label.setText("Pokémon not found!")

    def fetch_pokemon_info(self, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_info = {
                "name": pokemon_data["name"],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
                "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
            }
            pokemon_image_url = pokemon_data["sprites"]["front_default"] if pokemon_data["sprites"]["front_default"] else None
            return pokemon_info, pokemon_image_url
        else:
            return None, None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PokemonInfoApp()
    window.show()
    sys.exit(app.exec_())
