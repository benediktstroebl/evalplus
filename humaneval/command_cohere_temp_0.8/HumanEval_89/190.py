```python
def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 2
    for char in string:
        index = alphabet.find(char)
        next_index = (index + rotation) % len(alphabet)
        encrypted += alphabet[next_index]
    return encrypted
```
This encrypt function processes each character in the input string as follows:
1. It uses the `find` method to convert each character to its alphabetical index.
2. It adds the `rotation` value (which is 2) to advance through the alphabet.
3. It uses the modulo operator (`%`) to repeat the alphabet if needed.
4. It appends the shifted index value back to the `encrypted` string.

The overall effect is to encrypt the input string by shifting each character down by two places, wrapping around the alphabet.