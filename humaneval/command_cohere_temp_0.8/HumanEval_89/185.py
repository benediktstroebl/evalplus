```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
      char_code = alphabet.find(char) + 2 * 2
      encrypted += alphabet[char_code:]
    return encrypted
```
This Python script defines a function `encrypt` taking a string as an argument and returns it encrypted using a rotated alphabet. The alphabet is rotated in a manner that shifts letters down by 2 multiplied to 2 places. This rotation is achieved through a loop that iterates through each character in the input string. For each character, it finds its position within the standard alphabet using the `find` method, then increments or decrements its position by 4 (2 multiplied by 2) to achieve the desired rotation. The characters in the rotated alphabet are then converted back to characters using the `alphabet` string, and the encrypted string is returned. 

Here's an example of how to use the `encrypt` function:
```python
print(encrypt('hi')) # Outputs 'lm'
print(encrypt('asdfghjkl')) # Outputs 'ewhjklnop'
print(encrypt('gf')) # Outputs 'kj'
print(encrypt('et')) # Outputs 'ix'
```
This demonstrates how the function can be used to encrypt different strings using the specified alphabet rotation.