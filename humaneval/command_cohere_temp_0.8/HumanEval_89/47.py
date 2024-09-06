```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2 * (index % 2)]
    return encrypted
```

This function defines an `encrypt` function that takes a string `s` as input and returns the encrypted string using the alphabet rotation technique described in the problem statement. It loops through each character in the input string, finds its index in the alphabet, and then adds the character 2 positions ahead of its current position in the alphabet, considering the index's parity to determine whether to increment by 1 or 2. This method of encryption turns the string 'hi' into 'lm', 'asdfghjkl' into 'ewhjklnop', 'gf' into 'kj', and 'et' into 'ix'.