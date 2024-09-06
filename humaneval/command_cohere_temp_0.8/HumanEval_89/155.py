```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        if char in alphabet:
            idx = alphabet.find(char)
            encrypted.append(alphabet[(idx + rotation) % len(alphabet)])
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```
This Python script defines a function `encrypt` that takes a string `s` as input and returns an encrypted version of the string using a rotated alphabet. Here's how it works:
1. The `encrypt` function starts with an empty list called `encrypted` to store the encrypted characters.
2. It defines a constant `alphabet` that represents the full alphabet, namely "abcdefghijklmnopqrstuvwxyz."
3. The variable `rotation` is set to 2, indicating how many positions the alphabet will be rotated for each character.
4. Then, it iterates through each character in the input string `s`.
5. For each character, it checks if the character is present in the alphabet. If it is, it proceeds to encrypt it.
6. If the character is in the alphabet, it finds its index in the alphabet.
7. Then, it applies the rotation factor. It adds the `rotation` to the index and takes the modulus of the length of the alphabet to avoid indexing out of bounds or repeating characters. This gives the new index in the rotated alphabet.
8. The character from the rotated index is added to the `encrypted` list.
9. If the character is not in the alphabet, it's not encrypted and added to the list as is.
10. After processing all characters, the function joins the encrypted characters in the list into a string and returns the encrypted string.

The script ensures that non-alphabet characters remain unchanged, and the encryption process provides the specified rotation effect, encrypting using the rotated alphabet.