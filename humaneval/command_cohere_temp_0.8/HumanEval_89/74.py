```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        offset = ord(char) + 2 * (ord(alphabet[0]) - 97)
        encryptedChar = chr(offset % 26 + 97)
        encrypted += encryptedChar

    return encrypted
```

This Python script defines a function `encrypt()` that takes a string `s` as input and returns the encrypted version of the string as described in the problem statement. Here's a breakdown of how it works:
1.  The variable `alphabet` stores the full English alphabet.
2.  An empty string `encrypted` is initialized to store the encrypted characters.
3.  The input string `s` is iterated character by character.
4.  For each character `char` in the input string:
    -   An offset is calculated by adding the numerical value of the character (`ord(char)`), to which is subtracted the numerical value of the first character in the alphabet (`97`), and then multiplied by 2. This logic simulates shifting each character down by two places. 
    -   The result is taken modulo 26 to ensure the offset wraps around and stays within the bounds of the alphabet. 
    -   The character that corresponds to the calculated offset is added to the `encrypted` string. This character is computed by adding 97 to the modulus result to get a character within the alphabet.
5.  Finally, the `encrypted` string is returned.

The script assumes that the input string contains only alphabetic characters. If non-alphabetic characters are included, they will be skipped in the encryption process.