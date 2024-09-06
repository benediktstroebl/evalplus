def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_alphabet = alphabet[2:] + alphabet[:2]
    for char in string:
      encrypted+= rot_alphabet[alphabet.find(char)+1]
    return encrypted