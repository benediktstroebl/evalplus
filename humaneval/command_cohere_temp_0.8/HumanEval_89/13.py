```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        index = alphabet.find(letter)
        encrypted.append(alphabet[(index + 2 * 2) % 26])
    return ''.join(encrypted)
```
This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted version of the string. Inside the function, it initializes an alphabet string and iterates through each letter in the input. It uses the find method to determine the index of each letter in the alphabet and then encrypts it by shifting the index by 2 twice, wrapping around the alphabet size of 26. The encrypted letter is added to a list, which is joined into a string and returned as the result. 

Here is an example usage of the function and the expected output:
```python
print(encrypt('hi'))  # Expected output: lm
print(encrypt('asdfghjkl'))  # Expected output: ewhjklnop
print(encrypt('gf'))  # Expected output: kj
print(encrypt('et'))  # Expected output: ix
```
The expected output of the example usages matches the description provided in the problem statement.