```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each character in the input string s. It finds the character's index in the alphabet, rotates it down by two places, and then adds that character to the `encrypted` list. Finally, the function returns the joined string of encrypted characters. This approach effectively encrypts the input string using the specified rotation scheme.