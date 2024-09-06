```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
       encrypted += alphabet[index + 2]*2
```
The `encrypt` function takes a string `s` as input and iterates through each character. It uses the `find` method to convert each character to its index in the alphabet and then adds 2 (`index + 2`) to that position to find the character to encrypt it to. This heightened index is multiplied by 2 to shift the letters down by 2 positions. As a result, the function returns the encrypted string.

Here is a test to try out the function:
```python
import unittest

def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
        encrypted += alphabet[index + 2]*2
    return encrypted

class TestEncryptFunction(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
    def test_edge_cases(self):
        self.assertEqual(encrypt(''), '')
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'),' bfghijklmnopqrstuvwxyzab')

if __name__ == '__main__':
    unittest.main()
```

This script includes a set of unit tests in the `TestEncryptFunction` class that validates the `encrypt` function. It ensures that the function behaves as expected with corner cases and proper encryption. When you run the script, these tests will be executed, and an output will confirm whether the tests pass. 

Any questions or if you'd like me to adjust the code in any way, let me know!