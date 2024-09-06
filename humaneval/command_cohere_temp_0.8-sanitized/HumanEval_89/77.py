def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encodedString = []

    for char in string:
        index = alphabet.find(char)
        encodedString.append(alphabet[index + 2 * (ord(char) - 96) :: 2])

    return ''.join(encodedString)