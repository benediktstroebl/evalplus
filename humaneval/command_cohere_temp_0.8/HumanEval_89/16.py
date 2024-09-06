```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in string:
      char_index = alphabet.find(char)
      shifted_char_index = (char_index + 2) % len(alphabet)
      encrypted.append(alphabet[shifted_char_index])
    return ''.join(encrypted)
```
This Python script defines a function called `encrypt` that takes a string as input and iterates through each character in the string. It uses the `alphabet` variable to store the entire alphabet, and initializes an empty list called `encrypted` to store the encrypted characters. For each character in the input string, it searches for its position in the alphabet using the `find` method. It then calculates a shifted index by adding 2 to the current index and taking the modulus of the length of the alphabet. This ensures the rotation shifts down by two multiplied to two places. The character at the shifted index is added to the `encrypted` list, and finally, the function returns a joined string of all the encrypted characters.