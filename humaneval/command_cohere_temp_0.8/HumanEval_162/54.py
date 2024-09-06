```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function utilizes the `hashlib` module in Python which provides an implementation of cryptographic hash functions, including the MD5 hash algorithm. The function calculates the MD5 hash of the input text and returns its hexadecimal representation as a string, or `None` if the input text is empty. 

To test this function, you can use the following script:
```python
import hashlib
import unittest

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

class TestStringToMD5(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

if __name__ == '__main__':
    unittest.main()
```

In this test suite, the `test_basic` test verifies that the function correctly calculates the MD5 hash for the input string `'Hello world'`, and matches it with the expected hash value. Meanwhile, `test_empty_string` ensures that when an empty string is provided, the function returns `None`, as stated in the problem statement. 

The `unittest.main()` call executes the tests when this script is run directly. 

To run the test, ensure that the script is saved in the same directory and then execute it via the command line:
```bash
python test_string_to_md5.py
```

The output will indicate the successful execution of both test cases.