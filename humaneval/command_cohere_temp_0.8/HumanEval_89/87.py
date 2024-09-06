```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted.append(char)
        else:
            rotated_index = (index + 2) % 26
            encrypted.append(alphabet[rotated_index])
    return ''.join(encrypted)
```
This function uses the `alphabet` string, which stores all the possible characters to encrypt, and the modulo operator to ensure the rotation wraps around the alphabet when the index is reached. It iterates through the input string `s`, using the find method to identify the character's original index and then applies the rotation scheme to determine the new index. When a character is encountered that isn't in the alphabet, it's appended as is to the `encrypted` string without modification. Finally, the function returns the `encrypted` string. 

Here's an example usage of the function with a test case:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('foo') == 'prbazmoc'
    assert encrypt('bar') == 'rbazmotic'
```