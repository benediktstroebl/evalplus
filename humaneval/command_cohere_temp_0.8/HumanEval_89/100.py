```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```
This function uses a basic Caesar cipher technique to encrypt a string `s` by shifting letters in the alphabet by a specified number of places. In this case, the alphabet is shifted downward by two multiplied by two places. The function then returns the encrypted string by joining the encrypted characters together. 

Here is a simple test case to ensure the functionality of the function:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
```