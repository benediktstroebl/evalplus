```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotation = 2
    for char in s:
        if char.isalpha():
            offset = ord(char) - 96 + rotation // 2
            encrypted.append(chr(offset + 96))
        else:
            encrypted.append(char)
    return "".join(encrypted)
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet scheme. The algorithm:
1. Appends characters to the `encrypted` list, ignoring non-alphabet characters.
2. Uses the `alphabet` string and a `rotation` factor to calculate an `offset` for each character.
3. Adds the `offset` to the base value of 96 to obtain the encrypted character, ensuring it's within the `alphabet` range.
4. Joining the `encrypted` list yields the final encrypted string. 

This approach encrypts alphabetic characters in the input, shifting the alphabet vertically and horizontally using the defined `rotation` scheme. Non-alphabetic characters are left untouched in the encrypted string.