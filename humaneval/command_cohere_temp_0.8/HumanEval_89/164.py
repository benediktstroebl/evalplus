```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        index = alphabet.find(letter)
        encrypted.append(alphabet[(index + 2 * 2) % 26])
    return ''.join(encrypted)
```
This Python script defines a function `encrypt` taking a string s as an argument and returning an encrypted string using a rotated alphabet scheme. The alphabet is stored in the `alphabet` variable and is set to `abcdefghijklmnopqrstuvwxyz`. The function iterates through each letter in the input string s, finds the index of the letter in the alphabet, and then calculates a new index by adding 2 twice (down shifting by 2 positions, and wrapping around using modulo 26). It uses this new index to retrieve a new letter from the alphabet and appends it to the `encrypted` list. Finally, it joins the encrypted letters together into a single string and returns the encrypted string. 
The expected output for the given examples in the prompt would be:
```
lm
ewhjklnop
kj
ix
``` 
This solution employs only Python's built-in functionalities and does not require any external modules. It is self-contained and should work correctly for any input string s.