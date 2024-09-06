```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:] + alphabet[:2]
    for char in s:
      encrypted += rotated_alphabet[alphabet.find(char)]
    return encrypted
```

This function uses three main steps to solve the problem:
1. It defines the rotational alphabet that is shifted down by two multiplied to two places.
2. It iterates through each character in the original string.
3. It finds the character in the original alphabet and returns the equivalent in the rotated alphabet.

This approach allows the function to cleanly encrypt any string using the specified encryption algorithm. Feel free to ask any questions about the code or request any other modifications for improvements.