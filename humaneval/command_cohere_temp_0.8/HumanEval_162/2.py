```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains whitespace using the `strip` method, ensuring that leading and trailing whitespaces are accounted for. If the condition is met, it computes the MD5 hash of the text using the `md5` algorithm and returns the resulting hash as a hexadecimal string. If the input is empty or contains only whitespace, it returns `None`, following the problem's requirement. 

This approach ensures that empty inputs are handled correctly, and it produces the expected MD5 hash for non-empty texts. 

To verify the correctness of the function, you can use the following test case:
```python
import unittest
from bibtex_to_markdown import string_to_md5

class TestStringToMd5(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_whitespace_string(self):
        self.assertIsNone(string_to_md5('   '))

if __name__ == '__main__':
    unittest.main()
```
This test suite includes three test cases: one to test a standard non-empty string, one for an empty string, and one for a string that contains only whitespaces. 

NOTE: MD5 is no longer considered a secure hashing algorithm for password storage and cryptographic purposes, since it has vulnerabilities regarding collision resistance. It is present here for the sake of problem resolution and code example, however, in real-world scenarios, it is recommended to use more secure hashing algorithms like SHA-256 or Argon2.