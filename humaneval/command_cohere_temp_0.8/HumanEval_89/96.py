```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2]
    return encrypted
```
This Python script defines a function encrypt(string) that takes a string as input and outputs the encrypted version of the string according to the problem statement. Essentially, it shifts the alphabet downward by 2 steps, and then again by 2 steps for each character, effectively cycling through the alphabet with each character.