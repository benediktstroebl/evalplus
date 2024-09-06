```python
def encrypt(s):
    encrypted = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_index_map = {alphabet[i]: alphabet[i + 2 * s.count(alphabet[0])] 
                                for i in range(26)}
    for char in s:
      encrypted.append(rot_index_map[char])
    return ''.join(encrypted)
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet. The script first creates an empty list called `encrypted` to store the encrypted characters. It also defines the full alphabet `abcdefghijklmnopqrstuvwxyz` and a dictionary called `rot_index_map` to map each character in the plaintext to its corresponding rotated position in the encrypted text. This mapping is determined by the formula `i + 2 * s.count(alphabet[0])` which defines a linear descending shift in the alphabet, multiplying the shift by 2 after each character. 

Then, the script iterates over each character in the input string `s`. For each character `char`, it retrieves its corresponding encrypted character from the `rot_index_map` dictionary and appends it to the `encrypted` list. Finally, the script joins the encrypted list into a string and returns it. 

This code effectively implements the encryption described in the problem statement, shifting characters based on their frequency in the plaintext and the first character's position.