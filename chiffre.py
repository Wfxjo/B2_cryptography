
def ceaser_cryptography(text, key):
	crypted_text = ""
	for char in text:
			crypted_text += chr((ord(char) + key) % 0x110000)

	return crypted_text

def ceaser_decode(crypted_message, key):
	return ceaser_cryptography(crypted_message, -key)

message = "MARS"
crypted_message = ceaser_cryptography(message, 10652)
initial_message = ceaser_decode(crypted_message, 10652)

print(crypted_message)
print(initial_message)


# # Script pour crypter de 1 à 25
# crypted_text = "⧩⧝⧮⧯"

# for key in range(1, 26):
#     decoded = ceaser_decode(crypted_text, key)
#     print(f"difference {key}: {decoded}")






# Vigenere

def vigenere_crypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        shift = ord(key[key_index % key_length])
        char = chr((ord(char) + shift) % 0x110000)
        encrypted_text += char
        key_index += 1

    return encrypted_text

phrase = "Then what shall we Die for ?"
key = "AMOUR"
encrypted_phrase = vigenere_crypt(phrase, key)
print("Viginere :",encrypted_phrase)

# def vigenere_uncod(text, key):
#     return vigenere_crypt(text, key, decrypt=True)

# decode_phrase = vigenere_uncod(encrypted_phrase, key)
# print(decode_phrase)