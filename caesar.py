encrypted_text='khoor cdlud'
shift=3

def decrypt():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text=''

    for char in encrypted_text.lower():
        index=alphabet.find(char)
        new_index=(index - shift) % len(alphabet)
        text+=alphabet[new_index]
    print(text)

decrypt()