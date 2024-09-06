```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
       encrypted += alphabet[index + 2]*2
 # Test cases
assert encrypt('hi') == 'lm'
assert encrypt('asdfghjkl') == 'ewhjklnop'
assert encrypt('gf') == 'kj'
assert encrypt('et') == 'ix'
```
This code snippet defines the `encrypt` function which takes a string `s` as input and iterates through each character. Using the `find` method to find the character's index in the alphabet, the index is then incremented by 2 to determine the encrypted character. This encrypted character is then appended to the `encrypted` string and returned. 

The markdown code block above includes several test cases to ensure that the encrypt function behaves as expected. These tests can be run by adding the following test suite at the end of the script:
```python
import unittest

def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2]*2
    return encrypted

class TestEncryptFunction(unittest.TestCase):
    def test_hi(self):
        self.assertEqual(encrypt('hi'), 'lm')
    def test_asdfghjkl(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
    def test_gf(self):
        self.assertEqual(encrypt('gf'), 'kj')
    def test_et(self):
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()
```