```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2]

    return encrypted
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet. The algorithm achieves this by first creating an instance of the alphabet ('abcdefghijklmnopqrstuvwxyz') and then iterating through each character in the input string `s`. For each character, it finds its position in the alphabet and then constructs the encrypted string using the characters two positions after and the characters immediately before the original character, respectively. The result is a string that represents the input string encrypted using the rotated alphabet technique.