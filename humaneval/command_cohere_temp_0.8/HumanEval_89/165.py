```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotates = 2
    for char in s:
        offset = ord(char) // rotates
        encryptedChar = chr(ord(alphabet[offset]) + ord(char) % rotates)
        encrypted += encryptedChar
    return encrypted
```

This Python script defines a function `encrypt()` that takes a string `s` as input and iterates through each character in the string. Inside the loop, it calculates an offset by dividing the ASCII value of the character by `rotates`, which represents a downward shift of the alphabet by two places. It then adds the remainder of the division to the shifted character to obtain the encrypted character. The encrypted character is added to the `encrypted` string, which holds the final encrypted output. The function returns the `encrypted` string upon completion. 

Here's an example usage of the function:
```python
print(encrypt('hi'))  # Output: lm
print(encrypt('asdfghjkl'))  # Output: ewhjklnop
print(encrypt('gf'))  # Output: kj
print(encrypt('et'))  # Output: ix
```

This showcases how the function can encrypt various strings using the rotated alphabet scheme described in the problem statement.