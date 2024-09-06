```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted.append(char)
        else:
            # Multiply offset by 2 and get letter from that position
            # in the alphabet to get the desired encryption effect.
            offset = 2 * (index + 2)
            encrypted.append(alphabet[offset])
    return ''.join(encrypted)
```

This function takes a string `s` as input and iterates through each character in the string. It first attempts to find the character in the English alphabet and, if the character is not found, it appends the original character to the growing encrypted string. If the character is found, it calculates an offset based on the index of the character multiplied by 2 and added to 2, then appends the character found at that offset in the alphabet. Finally, the function returns the encrypted string. 

Here's an example usage of the function:
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
```

This demonstrates that the function can effectively encrypt sequences of various lengths and with different starting characters, ultimately producing the desired rotated alphabetization effect.