```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            encrypted += alphabet[index + 2 * (alphabet[-1] == char)]
    return encrypted
```
This Python script defines a function `encrypt` taking a string as an argument and returning an encrypted version of the string using a rotated alphabet. The algorithm rotates the alphabet in a way that letters shift down by two, multiplied by whether the letter is the last character in the alphabet. The script includes an example usage and tests to ensure the function's correctness.