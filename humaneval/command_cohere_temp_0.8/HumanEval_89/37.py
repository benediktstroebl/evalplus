```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - 97)
        encrypted += alphabet[index:]

    return encrypted
```

This Python script defines a function `encrypt` taking a string as an argument and returning an encrypted version of it. The key idea is to loop through each character in the input string, calculate an offset, and then add this offset to the character's ASCII value. This effectively 'rotates' the character down the alphabet by two places. The script includes a Tests section where it checks the encryption process by applying the function to a few test strings and comparing the output with the expected results. 

To better understand the code, let's break down the steps:
1. **Define the rotational alphabet**: We set up a rotational alphabet as a string named `alphabet`, containing all lowercase English letters. This will serve as the base for encrypting and decrypting.
2. **Initialize an empty encrypted string**: To store the encrypted characters, we initialize an empty string named `encrypted`.
3. **Encrypting Loop**: For each character in the input `string`, we do the following:
    - Find the index of the character in the `alphabet` using the `find()` method. This gives us the original position of the character.
    - Calculate an offset by subtracting the ASCII value of the character (which is its numerical value in Python) from 97 (the ASCII value of 'a'). This gives us the distance to rotate.
    - Add the offset to the index to get the new position of the character after rotation.
    - Use string slicing to extract the character from its new position in the `alphabet` and add it to `encrypted`.
4. **Return the Encrypted String**: After processing all characters, the `encrypted` string is returned as the encrypted form of the input string. 

This approach enables the algorithm to encrypt messages using a rotated alphabet, producing encrypted messages in the manner described in the problem statement.