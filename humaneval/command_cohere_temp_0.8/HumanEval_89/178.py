```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % 26
        char = alphabet[new_index]
        encrypted.append(char)
    return ''.join(encrypted)
```
This function uses a loop to iterate through each character in the input string `s`. It finds the index of each character in the alphabet, then calculates a new index by adding 2 twice and taking the modulus of 26. This ensures the alphabet rotates down by two positions with each character. It then assigns the character at the new index as the encrypted character and joins the encrypted characters into a single string.  It shifts the alphabet downwards by 2 positions with each character.