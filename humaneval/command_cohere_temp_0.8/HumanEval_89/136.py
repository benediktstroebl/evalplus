```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2) % 26
        char = alphabet[new_index]
        encrypted.append(char)
    return ''.join(encrypted)
```
This function uses a for loop to iterate through each character in the input string s. For each character, it finds its index in the alphabet, then calculates the new index after shifting down by two and wrapping around (using modular arithmetic), and finally appends the character at the new index to the encrypted list. The function then joins the encrypted list into a string and returns the encrypted version of the input string.