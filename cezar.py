rot = int(input("Zadej klíč: "))
action = input("Chceš [š]ifrovat nebo [d]ešifrovat?: ")
data = input("Zadej text: ")

if action == "š" or action == "šifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += rot   # rotujeme do prava == šifrujeme
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Šifra: '{}'".format(text))
elif action == "d" or action == "dešifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= rot   # rotujeme do leva == dešifrujeme
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("Text: '{}'".format(text))
else:
    print("Chyba! Špatná operace")
