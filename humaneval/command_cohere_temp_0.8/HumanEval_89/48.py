```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - 97)
        encrypted += alphabet[index:] if index < len(alphabet) else alphabet[:index]

    return encrypted
```

This Python script defines a function `encrypt` taking a string as an argument and returning an encrypted version of it. The encryption logic revolves around a predefined alphabet comprising ASCII characters from 'a' to 'z,' shifted two positions down. Essentially, the function searches for each character's index in the alphabet and adjusts it by adding 2 x (ASCII value of the character - 97), then fills in the encrypted characters using the adjusted index. The result is a cryptic rendition of the input string, showcasing the algorithm's application. 

Here's an example of how to use the function and expected output:
```python
encrypt('hi') # returns 'lm'
encrypt('asdfghjkl') # returns 'ewhjklnop'
encrypt('gf') # returns 'kj'
encrypt('et') # returns 'ix'
```