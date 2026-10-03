ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.lower() in ALPHABET:

            #where is the letter (0-25)
            position = ALPHABET.find(ch.lower())

            #move forward
            #wrap around
            new_position = (position + shift) % 26
            new_letter = ALPHABET[new_position]
            result += new_letter.upper() if ch.isupper() else new_letter
        else:
            #keep spaces, punctuation
            result += ch
    return result



def decrypt(text, shift):
    return encrypt(text, -shift)