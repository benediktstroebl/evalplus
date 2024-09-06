```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
      char_code = alphabet.find(char) + 2 * 2
      encryptedchar = alphabet[char_code % 26]
      encrypted += encryptedchar
    return encrypted
```
This function uses a loop to iterate through each character in the input string. For each character, it calculates a new value by adding two (the shift amount) to the index of the character in the alphabet, and then repeating this result for the next two places. This is done to ensure that the rotation is consistent for all the characters. It then uses this value to index the alphabet string to get the corresponding encrypted character and append it to the `encrypted` string.  This process results in an encrypted string that fulfills the criteria stated in the problem.