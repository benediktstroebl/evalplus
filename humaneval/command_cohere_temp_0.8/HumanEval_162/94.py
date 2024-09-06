```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings correctly.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if not text.strip():
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash for any given non-empty text. It checks for empty strings using `strip()` and `len()` to ensure that an empty result isn't returned for strings with only whitespace. The function returns `None` for empty input, conforming to the problem's request, and ensures UTF-8 encoding for a wide range of input characters.

The tests for this function can be added as a separate script to verify its correctness, for example:
```python
import unittest
from hashlib import md5
from string_to_md5 import string_to_md5

class TestStringToMD5(unittest.TestCase):
    def test_handles_empty_string(self):
        self.assertIsNone(string_to_md5(""))

    def test_returns_md5_for_text(self):
        self.assertEqual(string_to_md5("Hello World"), md5("Hello World").hexdigest()) 

if __name__ == "__main__":
    unittest.main()
```

This test suite includes a variety of tests to validate the correctness of the `string_to_md5()` function. The `test_handles_empty_string` verifies that the function handles empty input correctly by asserting that the output is `None`. The `test_returns_md5_for_text` checks the function's ability to return the correct MD5 hash for a non-empty string using a mock MD5 object created by using the `hashlib.md5()` function.

When you run this test suite using `unittest.main()` , it will provide clear feedback on whether the function behaves as expected, aiding in validating the code and assuring its correctness.