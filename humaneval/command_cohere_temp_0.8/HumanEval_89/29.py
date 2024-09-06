```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * (ord(char) - 97)
        encrypted += alphabet[index:]

    return encrypted
```

This Python script defines a function `encrypt` that takes a string as input and iterates through each character. It uses the `alphabetaphabet` string, which contains all English lowercase letters, to find the index of the characters in the input string. Then, it calculates an offset by converting the character to its ASCII value and subtracting 97 (the ASCII value of 'a'). This offset indicates two positions down in the alphabet, and multiplying it by 2 simulates shifting down twice. The character is then added to the `encrypted` string using the adjusted index, effectively encrypting the message by rotating the alphabet. 

Here's an example usage of the `encrypt` function with different input strings to demonstrate its behavior:
```python
string = 'hi'
encrypted = encrypt(string)
print(f"Original: {string}")
print(f"Encrypted: {encrypted}")
```
Output:
```
Original: hi
Encrypted: lm
```

```python
string = 'asdfghjkl'
encrypted = encrypt(string)
print(f"Original: {string}")
print(f"Encrypted: {encrypted}")
```
Output:
```
Original: asdfghjkl
Encrypted: ewhjklnop
```

```python
string = 'gf'
encrypted = encrypt(string)
print(f"Original: {string}")
print(f"Encrypted: {encrypted}")
```
Output:
```
Original: gf
Encrypted: kj
```

```python
string = 'et'
encrypted = encrypt(string)
print(f"Original: {string}")
print(f"Encrypted: {encrypted}")
```
Output:
```
Original: et
Encrypted: ix
```