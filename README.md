# Pokemon-Information-App-with-PyQt5
Description:
This Python script utilizes the PokeAPI to fetch information about a specified Pokémon and displays it in a graphical user interface (GUI) built using PyQt5. The app allows users to input a Pokémon's name and retrieves its details such as name, height, weight, abilities, and types from the PokeAPI.

Features:

Utilizes PyQt5 for GUI development.
Fetches Pokémon details (name, height, weight, abilities, types) from the PokeAPI.
Displays Pokémon information along with its image fetched from the PokeAPI.
Dynamically adjusts the displayed image to fit the window size while maintaining its aspect ratio.
Key Components:

PyQt5 for GUI layout and functionality.
requests library to interact with the PokeAPI.
QLabel, QLineEdit, QPushButton for UI elements.
Utilizes QPixmap to display fetched Pokémon images.
Usage:

Run the Python script.
Enter the name of the Pokémon in the input field.
Click the "Get Info" button to fetch and display the Pokémon's details along with its image.
Instructions:

Install PyQt5 and requests libraries if not already installed (pip install PyQt5 requests).
Run the script and input the name of the Pokémon when prompted.
The app will display the Pokémon's information and image if found; otherwise, it will show a "Pokémon not found!" message.
Notes:

This script assumes an active internet connection to fetch data from the PokeAPI.
Ensure proper Python dependencies are installed before running the script.
Additional Information:

Python version: 3.x
Libraries used: PyQt5, requests
Contributions:
Contributions, bug reports, and feedback are welcome. Feel free to fork and create pull requests for enhancements or bug fixes.
