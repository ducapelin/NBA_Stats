alphabet = "abcdefghijklmnopqrstuvwxyz"
list_alphabet = list(alphabet)

def cripto(word):
    word_cripto = []
    for letter in word:
        word_cripto.append(str(list_alphabet.index(letter) + 1))
    return word_cripto

print(cripto("malaco"))
