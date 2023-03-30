#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        list_of_user = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry Only letters ")
        generate_phonetic()
    else:
        print(list_of_user)


generate_phonetic()