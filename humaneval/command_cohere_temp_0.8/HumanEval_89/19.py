```python
def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted.append((char + 2) % 26)
            else:
                encrypted.append((char + 2) % 26 + 96)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This Python script defines a function called `encrypt` that takes a string `s` as input. It iterates through each character in the string, checking if each character is alphabetical. If it is, it performs an encryption algorithm and appends the encrypted character to the `encrypted` list. Finally, it joins the encrypted list to return the encrypted string. 

The encryption algorithm shifts each alphabetical character two positions down the alphabet, and in the case of lowercase letters, it wraps around to the end of the alphabet and continues from the opposite end, due to the condition `% 26`. Would you like to know more about how this code works, or about any of the concepts presented in it?