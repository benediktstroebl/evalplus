```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings.

    Args:
        text (str): The input string.

    Returns:
        str or None: MD5 hash if text is not empty, otherwise None.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` Python module to calculate the MD5 hash of the input string. The function handles empty input strings by returning `None`.

To test this function, you can use the provided test case:
```python
def test_string_to_md5():
    """
    Tests:
    1. String is encrypted correctly.
    2. Empty string returns None.
    """
    assert string_to_md5("Hello World!") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
```

You can run these tests by adding them to a Python script and running the script.  The `string_to_md5` function will correctly handle empty strings and return the MD5 hash for non-empty strings. 

**NOTE:** MD5 hash is not secure and is vulnerable to collisions. If security is a concern, consider using hash functions like SHA-256 instead.