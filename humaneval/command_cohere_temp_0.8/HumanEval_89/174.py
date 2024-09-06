```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_index_map = {alphabet[i]: alphabet[i + 2 * s.count(alphabet[0])] 
                      for i in range(26)}
    for char in s:
        if char in alphabet:
            encrypted.append(rot_index_map[char])
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This Python script defines a function `encrypt` taking a string `s` as input and returning a string encrypted according to the problem statement. 

The script creates an `encrypted` list to store the elements of the encrypted string. It also defines an `alphabet` containing all lowercase letters, and a dictionary `rot_index_map` that maps each letter to its rotated counterpart. The rotation amount is determined by `s.count(alphabet[0])`, which represents the repetition count of the most frequent letter in `s`. This ensures the alphabet shifts down by two places.

Then, the script iterates through each character in `s`. If the character is in the alphabet, the script retrieves its rotated counterpart from the `rot_index_map` and adds it to `encrypted`. If the character is not in the alphabet, it's added to `encrypted` as-is. Finally, the function joins the elements of `encrypted` to form the encrypted string and returns the result.