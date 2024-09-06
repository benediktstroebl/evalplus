```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_idx = 2
    for char in s:
        encrypted_char = alphabet[alphabet.find(char) + rot_idx]
        encrypted = encrypted + encrypted_char
    return encrypted
```
This Python script defines a function `encrypt` using a for loop to iterate through each character in the input string `s`. For each character, it rotates the alphabet by `rot_idx` positions to encrypt the character and then appends the encrypted character to the `encrypted` string. The script provides an accurate solution to the problem statement, resulting in an encrypted string using the specified rotated alphabet. 
The alphabet is stored in the character variable `alphabet` and the rotation index is stored in the integer variable `rot_idx`. This allows for consistency and avoids hardcoding the rotation value throughout the loop. 
The script returns the encrypted string when the loop has finished iterating through all characters in the input string. This solution is efficient, with a time complexity of O(n), where n is the length of the input string s, due to the loop iterating through each character once.