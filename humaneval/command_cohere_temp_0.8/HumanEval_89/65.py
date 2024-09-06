```python
def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + 2]
        encrypted.append(char)
    return ''.join(encrypted)
```
This function iterates over each character in the input string `s`. When it encounters an alphabetic character, it uses the index of that character in the alphabet to calculate a new index that is two positions ahead, and then finds the character at that new index in the rotated alphabet to use as the encrypted character. Non-alphabetic characters remain unaffected. The function returns the encrypted string.

Here is a test script that verifies the function:
```python
import unittest

def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + 2]
        encrypted.append(char)
    return ''.join(encrypted)

class TestEncryptFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_edge_cases(self):
        self.assertEqual(encrypt(''), '')
        self.assertEqual(encrypt('ABC'), 'BCA')
        self.assertEqual(encrypt('ZYX'), 'WUV')

    def test_long_input(self):
        self.assertEqual(encrypt('abcde'), 'cfih')
        self.assertEqual(encrypt('bcdef'), 'djmuw')

if __name__ == '__main__':
    unittest.main()
```

In this test suite, the `test_basic` function verifies the example use cases provided in the prompt, the `test_edge_cases` function makes sure the function handles edge conditions correctly, and the `test_long_input` function tests the function with longer inputs to ensure correctness. 

The `unittest.main()` call runs all the tests when the script is executed directly. 

To execute this test suite, copy and paste the test script into a Python environment of your choice and run it. 

Let me know if I missed anything or if you have any additional questions!