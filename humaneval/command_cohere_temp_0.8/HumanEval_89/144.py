```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_amount = 2 * 2
    for char in s:
        if char.isalpha():
            char_code = alphabet.find(char)
            encrypted_char_code = (char_code + rotate_amount) % len(alphabet)
            encrypted += alphabet[encrypted_char_code]
        else:
            encrypted += char
    return encrypted
```

This code snippet defines a function `encrypt` that takes a string `s` as input and returns a string with each alphabetical character encrypted using a rotated alphabet scheme. The encryption process is depicted in the following steps:
1. Define a variable `encrypted` to store the encrypted message and an `alphabet` that contains all alphabetical characters.
2. Set a constant `rotate_amount` to determine the rotation frequency for characters.
3. Iterate through each character in the input string `s`.
4. If the current character is an alphabet letter, proceed with the encryption; otherwise, append the character to the `encrypted` string as is.
5. Locate the alphabetical character's position in the `alphabet` using the `find` method.
6. Calculate the encrypted character's code by adding `rotate_amount` to the current character's code and taking the modulus of the string's length. This ensures the rotation repeats through the alphabet.
7. Append the encrypted character (the character at the calculated code in the `alphabet`) to the `encrypted` string.
8. Return the encrypted string.

This encryption algorithm, especially when combined with additional security measures, can be an essential component of many encryption applications.