```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            rotated_index = (index + 2) % 26
            encrypted += alphabet[rotated_index]
    return encrypted
```
This function uses the string 'abcdefghijklmnopqrstuvwxyz' to map characters to their rotated index. It iterates through each character in the input string and uses the find method to locate the original position of the character in the alphabet. If the character is not found (punctuation), it is appended as is in the encrypted string. Otherwise, the function calculates the offset to determine the new position of the character after a rotation, and repeatedly rotates the index (using modulus 26) until it reaches a valid ASCII character. Ultimately, the function returns a string with the encrypted characters.