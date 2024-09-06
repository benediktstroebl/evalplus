```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the hashlib library in Python to calculate the MD5 hash of the input text. The function encodes the input string to UTF-8 format before creating an MD5 hash object. Using the .update() method, it updates the hash object with the encoded string, and then the .hexdigest() method returns the hash in hexadecimal format.

To handle empty input strings, the function returns None.

To verify the correct behavior of the function, you can use the following tests:
```python
# Test for an empty string
assert string_to_md5("") is None

# Test for a non-empty string
assert string_to_md5("Hello World") == "3e25960a79dbc69b674cd4ec67a72c62"
```

The first test ensures that the function returns None for an empty input string, while the second test verifies that the function correctly calculates the MD5 hash for the string "Hello World" and matches it with the expected hash value.