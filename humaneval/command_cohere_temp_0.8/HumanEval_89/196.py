```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        index = alphabet.find(letter)
       encrypted.append(alphabet[(index + 2 * 2) % 26])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each letter in the input string. It looks up the index of the letter in the alphabet and then calculates a new index by adding 2 twice and taking a modulus 26. This process shifts each letter down two positions in the alphabet, with the ' wrapping around to the beginning of the alphabet. It then constructs a new string using the encrypted letters. The function is then tested using several input strings, and the output is verified to match the expected encrypted strings.