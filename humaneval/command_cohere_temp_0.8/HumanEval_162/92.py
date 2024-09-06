```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input is empty.
    """
    if text and text.strip():
        # Remove all non-ASCII characters
        text = ''.join(char if char.isascii() else ' ' for char in text)
        # Create an MD5 hash and encode it as a hexadecimal string
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to generate an MD5 hash, it first checks if the input string is empty or not. If the input string is empty, it returns None. Otherwise, it removes all non-ASCII characters from the string and then creates an MD5 hash with the modified string. The resulting hash is returned as a hexadecimal string. 

To verify the correctness of the implementation, you can run the following tests:
```python
# Test with a non-empty string
assert string_to_md5("Hello World!") == "3e25960a79dbc69b674cd4ec67a72c62"

# Test with an empty string
assert string_to_md5("") is None
```

These tests will ensure that the `string_to_md5` function works correctly for both empty strings and non-empty strings.