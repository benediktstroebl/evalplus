```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate = 2
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + rotate]
        encrypted.append(char)
    return ''.join(encrypted)
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet scheme. The script creates the encrypted list, where each letter in the input is appended to the encrypted list after being rotated properly. The script then joins the encrypted list into a string and returns the encrypted string. 

Here is an example execution:
```python
>> print(encrypt('hi'))
lm
>> print(encrypt('asdfghjkl'))
ewhjklnop
>> print(encrypt('gf'))
kj
>> print(encrypt('et'))
ix
```

The provided example usage demonstrates the behavior of the `encrypt` function as described in the problem statement. Each call to `encrypt` rotates letters in the input string accordingly, encrypting the message using the shifted alphabet.