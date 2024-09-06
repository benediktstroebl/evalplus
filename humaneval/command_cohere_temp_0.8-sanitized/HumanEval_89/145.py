def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Find the offset by calculating the character's ASCII value modulo the length of the alphabet
        # Adding the offset to the alphabet's start rotates the alphabet by the desired amount
        offset = (alphabet.index(char) + 2 * (ord(char) % len(alphabet))) % len(alphabet)
        encrypted.append(alphabet[offset])
    return ''.join(encrypted)