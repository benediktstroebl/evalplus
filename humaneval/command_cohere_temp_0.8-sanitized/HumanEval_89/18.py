def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        # Adding two to the index and expressing it modulo the length of the alphabet
        # Then using the character at that new index in the encrypted message
        encrypted += alphabet[index + (index // 2) :: 2]

    return encrypted