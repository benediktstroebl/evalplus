```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Args:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input is empty.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` Python module to calculate the MD5 hash of the input string. The function encodes the text into bytes using the UTF-8 encoding and then generates the hash digest using the `hashlib.md5()` function. The resulting hash is then converted to a hexadecimal string using `hexdigest()`, which is returned as the result.

If the input is an empty string, the function returns `None`. 

Here's an example of how you can use this function:
```python
def test_string_to_md5():
    """
    Test the string_to_md5 function.
    """
    assert string_to_md5("Hello World") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
    assert string_to_md5("foo") != "3e25960a79dbc69b674cd4ec67a72c62"
```

You can run this test case to validate the function.  This function can be used as a standalone MD5 encryption utility for any string data in your Python projects.