```python
def encrypt(s):
    encrypted = []
    for char in s:
        if char.isalpha():
            char = str(ord(char) - 96 + 8)
            encrypted.append(char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

This function takes a string `s` as input and returns a string encrypted using the specified encryption algorithm. It iterates through each character in the input string and checks if the character is an alphabet letter using the `isalpha()` method. If it is, the character's ordinal value is reduced by 96 (to adjust for the rotated alphabet) and increased by 8 (to adjust for the second shift), converting it to a letter in the desired rotated alphabet. The character is then appended to the `encrypted` list. If the character is not an alphabet letter, it's directly added to the `encrypted` list. Finally, the function joins the encrypted letters to return the encrypted string. 

To ensure the function's correctness, a set of tests is provided below:
```python
import unittest

class TestEncryptFunction(unittest.TestCase):
    def test_encrypt_hi(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_encrypt_asdfghjkl(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_encrypt_gf(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_encrypt_et(self):
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()
```

These unit tests cover various scenarios of the `encrypt` function with different input strings. Each test case is comprised of an input string and the expected encrypted string, which are stored in the `test_encrypt_hi`, `test_encrypt_asdfghjkl`, `test_encrypt_gf`, and `test_encrypt_et` methods. 

When the `unittest` module runs this class, it will execute each test case and verify if the output of the `encrypt` function matches the expected value. Any incorrect results will cause the test to fail, alerting the user to the need for further analysis or adjustment.  This test suite can be executed directly in Python by running `python TestEncryptFunction.py` at the command line.  This approach simplifies the process of testing and validating code changes, ensuring the function's behavior matches the described problem statement.  Any errors or unexpected behavior can be addressed to properly solve the problem.