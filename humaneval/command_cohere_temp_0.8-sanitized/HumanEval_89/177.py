import unittest
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        index = alphabet.find(char)
        encrypted.append(alphabet[index+2*(index%2)])
    return ''.join(encrypted)