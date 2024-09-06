```python
def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate_by = 2 * 2

    for char in string:
        index = alphabet.find(char)
        new_index = (index + rotate_by) % len(alphabet)
        encrypted += alphabet[new_index]
    return encrypted
```

This encrypt function takes a string as input and iterates through each character. It uses the `find()` method to convert each character to its index in the alphabet and then calculates the new index after rotation, wrapping around using the modulo operator. Finally, it concatenates the encrypted characters to form the output. The expected output is as specified in the problem statement.