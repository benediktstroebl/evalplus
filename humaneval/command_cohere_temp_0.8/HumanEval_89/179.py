```python
def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encodedString = []

    for char in string:
        index = alphabet.find(char)
        encodedString.append(alphabet[index + 2 * (ord(char) - 96) :: 2])

    return ''.join(encodedString)
```

This Python script defines a function called `encrypt` that takes a string as input and encrypts it using a rotated alphabet scheme. Here's how it works:
1. The `encrypt` function takes a string called `string` as input.
2. A variable named `encrypted` is initialized as an empty string. This will hold the encrypted message.
3. The alphabet `'abcdefghijklmnopqrstuvwxyz'` is defined for easy reference.
4. An empty list named `encodedString` is created to store the encrypted characters. This is done to simplify the process of shifting characters by two places.
5. The code iterates through each character (`char`) in the input string.
6. It finds the index of the character in the alphabet using the `find` method. This gives the relative position of the character in the alphabet.
7. The code shifts this position by 2 places either way, effectively wrapping around the alphabet, and encodes the character accordingly.
8. The shifted character is appended to `encodedString`.
9. After processing all characters, the encoded string is joined back together to form the encrypted message, and the result is returned as the output of the `encrypt` function.

This solution is straightforward and effectively encrypts the input string using the specified rotated alphabet scheme.