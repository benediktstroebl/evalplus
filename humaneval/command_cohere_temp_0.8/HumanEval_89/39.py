```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[(index + 2) % 26]

    return encrypted
```

This function uses a basic Python encryption technique. It rotates the alphabet used to encrypt a given string `s` by shifting each character two positions down the alphabet, looping back to the beginning of the alphabet when reaching the end. This is achieved by defining a constant `alphabet` string containing all lowercase letters. The function then loops through each character in the input string `s`, finding its index in the `alphabet`, and then performs the rotation logic `(index + 2) % 26` to encrypt the character. The resulting encrypted string is then returned.  This approach is simple and easy to understand, but it's important to note that like any basic encryption technique, it can be susceptible to brute-force attacks if used for cryptographic purposes.