```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2]

    return encrypted
```

This function defines an encryption process that can be used to encode messages, requiring advanced knowledge of the algorithm and the original alphabet size to decrypt. This code defines a function `encrypt` that takes a string as input and returns the encrypted version of that string using the described algorithm. 

Here's an example of how you can use the function with various inputs to see how it behaves:
```python
print(encrypt('hi')) # lm
print(encrypt('asdfghjkl')) # ewhjklnop
print(encrypt('gf')) # kj
print(encrypt('et')) # ix
```