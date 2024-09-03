```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[(index + 2) % 26]

    return encrypted
```

This function uses a basic Caesar cipher algorithm to encrypt a string by shifting letters two positions down the alphabet, wrapping around to the beginning of the alphabet if necessary. It iterates through each character in the input string, finds its index in the alphabet, and then adds 2 (or 2 modulo 26, to handle wrapping). This character at the new index in the alphabet is then appended to the `encrypted` string, building up the encrypted result. The algorithm is self-contained within the function and provides an easy-to-understand solution to the problem as asked.