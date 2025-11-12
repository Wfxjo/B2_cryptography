# import string


def ceaser_cryptography(text, key, cipher):
    if type(text) or str and type(key) or int:
	    return "".join([chr((ord(char) + (1 if cipher else -1) * key) % 1_114_112)\
                                                                for char in text])
    else:
        raise(TypeError)


def hack_cesar_cryptography(crypted_text, alphabet, cipher):
    if type(crypted_text) or str and type(alphabet) and str:
        for possible_key in range(0, 1_114_112):
            possible_uncryption = ceaser_cryptography(crypted_text, possible_key, cipher=False)
            if possible_uncryption[0] in alphabet:
                print(possible_key)
                print(possible_uncryption)
                print("_"*20)

    else:
        raise(TypeError)


def vigenere_cipher(text, password, cipher):
    list_of_keys = [ord(char) for char in password]
    list_of_crypted_chars = []
    for index, current_char in enumerate(text):
       
        current_key = list_of_keys[index % len(list_of_keys)]
        current_crypted_char = ceaser_cryptography(current_char, current_key, cipher)
    
        list_of_crypted_chars.append(current_crypted_char)

    crypted_text = "".join(list_of_crypted_chars)

    return (crypted_text)


if __name__ == "__main__":
    # text = "MARS"
    # crypted_text = ceaser_cryptography(text, 10652,cipher=True)
    # initial_text = ceaser_cryptography(crypted_text, 10652, cipher=False)

    # print(crypted_text)
    # print(initial_text)

    # Vigenere
    text = "Then what shall we Die for ?"
    key = "Hoist the Colours!"
    
    crypted_text = vigenere_cipher(text, key, cipher=True)
    print("coded message vigenere :", crypted_text)

    initial_text = vigenere_cipher(crypted_text, key, cipher=False)
    print("initial message vigenere :", initial_text)


