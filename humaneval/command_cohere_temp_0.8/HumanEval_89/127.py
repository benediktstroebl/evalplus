```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
      char_code = alphabet.find(char) + 2 * 2
      encrypted += alphabet[char_code % 26]
    return encrypted
```
This Python script defines a function called `encrypt` that takes a string as input and encrypts it using a rotated alphabet scheme. 

The script first creates a variable `alphabet` containing the entire English alphabet and then initializes an empty string called `encrypted` to store the encrypted message. 

The `encrypt` function iterates through each character of the input string. For each character, it calculates a new position in the alphabet using a formula of `alphabet.find(char) + 2 * 2`. This formula translates the original letter to a new position in the alphabet, shifting down two times by two places. Then, it adds the character at this new position modulo 26, which ensures that only letters within the alphabet are used, to the `encrypted` string. 

Finally, the function returns the `encrypted` string containing the encrypted message.