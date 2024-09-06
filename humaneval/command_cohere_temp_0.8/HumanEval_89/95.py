```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
        encrypted.append(alphabet[(index + 2 * 2) % 26])
    return ''.join(encrypted)
```
This Python script defines a function `encrypt` taking a string s as input and returning an encrypted string using a shifted alphabet. The alphabet is stored in the variable `alphabet`, initialized as the standard English alphabet. The function iterates through each character in the input string s, finds its index in the alphabet, and then calculates a new index by adding 2 (the downward shift amount) and then multiplying by 2 (if the result exceeds 26, to loop around the alphabet). The character at this new index in the alphabet is appended to the `encrypted` list, and finally, the function returns the joined encrypted string. 

Here is an example usage of the `encrypt` function taking a string with various lengths and characters to demonstrate how it rotates the alphabet to encrypt the message.
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
```
Which outputs:
```
lm
ewhjklnop
kj
ix
```
This demonstrates that the encrypt function shifts the alphabet downwards by two multiplied to two places, rotating the alphabet to encrypt the input string s.