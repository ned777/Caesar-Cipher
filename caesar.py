encrypted_text = 'Khoor Cdlud'
shift = 3

def decrypt():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ''

    for char in encrypted_text:
        if char.islower():
            index = lowercase.find(char)
            new_index = (index - shift) % len(lowercase)
            text += lowercase[new_index]
        elif char.isupper():
            index = uppercase.find(char)
            new_index = (index - shift) % len(uppercase)
            text += uppercase[new_index]
        else:
            # keep spaces, punctuation, numbers
            text += char

    print("decrypted:", text)

decrypt()