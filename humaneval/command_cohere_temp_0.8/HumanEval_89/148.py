```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        index = alphabet.find(char)
       encrypted.append(alphabet[index+2*(index%2)]);
    return ''.join(encrypted)
```
This function uses a temporary list 'encrypted' to iterate through each character in the input string. It then finds the character's index in the alphabet and shifts it downwards by two positions, alternating between positive and negative, and concatenates the result back into a string. 

Here is a test to try out the function:
```python
import unittest

def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        index = alphabet.find(char)
        encrypted.append(alphabet[index+2*(index%2)])
    return ''.join(encrypted)

class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
    def test_edge_cases(self):
        self.assertEqual(encrypt(''), '')
        self.assertEqual(encrypt('ABC'), 'LM')
        self.assertEqual(encrypt('ZYX'), 'VWX')
        self.assertEqual(encrypt('Some uppercase'), 'LjkjihkEff')
if __name__ == '__main__':
    unittest.main()
```
This test suite contains two test functions: 'test_encrypt' checks if the function works correctly for various inputs, and 'test_edge_cases' ensures that the function handles edge conditions correctly.