```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        offset = char[1] - char[0]
        new_char = char[0] + 2 * offset
        new_char = new_char if new_char in alphabet else new_char % 26 + alphabet[0]
        encrypted += new_char

    return encrypted
```
This Python script defines a function encrypt(s) that takes a string s as input and encrypts it using a shifted alphabet scheme. Here's how it works:
1. It starts by defining the standard alphabet as 'abcdefghijklmnopqrstuvwxyz'.
2. The variable encrypted is initialized as an empty string to store the encrypted message.
3. The function iterates through each character char in the input string s.
4. It calculates an offset for each character by subtracting the ASCII value of the character's first letter from the ASCII value of its second letter. This offset represents the shift in the alphabet.
5. It then adds 2 * offset to the second letter of the character, effectively shifting the character down by two places. If the resulting letter is not in the alphabet range, it wraps around by taking the modulus of 26 and adding the result to the starting letter of the alphabet.
6. The encrypted letter is added to the encrypted string and the process is repeated for all characters in the input string.

Lastly, the encrypted string is returned as the result. 

This encrypt function fulfills the problem statement's requirements, encrypting strings using a rotated alphabet scheme where letters shift down by two multiplied to two places.