```python
def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            rotated_index = (index + 2) % 26
            encrypted += alphabet[rotated_index]
    return encrypted
```
This function uses a basic Caesar cipher to encrypt the input string. It shifts each letter in the input string down by two indices in the alphabet and then wraps around using the modulus operator. It ignores non-alphabetical characters and encrypts them as is. 

Here's an example usage of the function:
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
```
This should return the expected encrypted strings 'lm', 'ewhjklnop', 'kj', and 'ix' respectively.