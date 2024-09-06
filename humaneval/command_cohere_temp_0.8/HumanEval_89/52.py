```python
def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_index_map = {alphabet[i]: alphabet[i + 2 * 2] for i in range(26)}
    for char in string:
        encrypted += rot_index_map[char]
    return encrypted
```

This function uses a basic substitution cipher to encrypt the given string. The alphabet is rotated in a way that each letter is shifted down by two multiplied by two places. The rotation is achieved through a dictionary where the key is the character of the original alphabet and the value is the character of the rotated alphabet. The loop iterates through each character in the string, and each character is replaced by its corresponding rotated character. The outcome is a string that contains the encrypted message.  This approach provides a concise solution that fulfills the challenge requirements.