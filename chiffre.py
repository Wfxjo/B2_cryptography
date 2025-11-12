# import string


def ceaser_cryptography(text, key):
    if type(text) or str and type(key) or int:
	    return "".join([chr((ord(char) + key) % 1_114_112) for char in text])
    else:
        raise(TypeError)

def ceaser_decode(crypted_text, key):
	return ceaser_cryptography(crypted_text, -key)


def hack_cesar_cryptography(crypted_text, alphabet):
    if type(crypted_text) or str and type(alphabet) and str:
        for possible_key in range(0, 1_114_112):
            possible_uncryption = ceaser_decode(crypted_text, possible_key)
            if possible_uncryption[0] in alphabet:
                print(possible_key)
                print(possible_uncryption)
                print("_"*20)

    else:
        raise(TypeError)



text = "MARS"
crypted_text = ceaser_cryptography(text, 10652)
initial_text = ceaser_decode(crypted_text, 10652)

print(crypted_text)
print(initial_text)


def convert_password_to_list_of_keys(password):
    return [ord(char) for char in password]



# if __name__ == "__main__":
#     message = "le chocolat est bon"

#     crypted_text = ceaser_cryptography(message,12) #exo1
#     print(crypted_text)

#     initial_message = ceaser_decode(crypted_text,12) #exo2
#     print(initial_message)

#     hack_cesar_cryptography(crypted_text, alphabet=string.printable) #exo3

# print(convert_password_to_list_of_keys("Azerty12345"))





# Vigenere


def vigenere_cipher(text, password):
    list_of_keys = [ord(char) for char in password]
    crypted_text = []
    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_text.append(ceaser_cryptography(char, current_key))

    return "".join(crypted_text)

phrase = "Then what shall we Die for ?"
key = "AMOUR"
encrypted_phrase = vigenere_cipher(phrase, key)
print("Viginere :",encrypted_phrase)




# def vigenere_crypt(text, key):
#     encrypted_text = ""
#     key_length = len(key)
#     key_index = 0

#     for char in text:
#         shift = ord(key[key_index % key_length])
#         char = chr((ord(char) + shift) % 0x110000)
#         encrypted_text += char
#         key_index += 1

#     return encrypted_text

# phrase = "Then what shall we Die for ?"
# key = "AMOUR"
# encrypted_phrase = vigenere_crypt(phrase, key)
# print("Viginere :",encrypted_phrase)






# def vigenere_uncod(text, key):
#     return vigenere_crypt(text, key, decrypt=True)

# decode_phrase = vigenere_uncod(encrypted_phrase, key)
# print(decode_phrase)


