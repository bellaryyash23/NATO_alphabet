import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def create_nato():
    input_word = input("Enter a word: ").upper()
    try:
        print([nato_alpha_dict[letter] for letter in input_word])
    except KeyError:
        print("Sorry, only letters in alphabet please")
        create_nato()


create_nato()
