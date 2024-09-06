```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

# Tests
md5_test = string_to_md5('Hello world')
assert md5_test == '3e25960a79dbc69b674cd4ec67a72c62'

empty_test = string_to_md5('')
assert empty_test is None
```

The `hashlib` module is used to generate the MD5 hash. Text is passed to the `update` function, and the `hexdigest()` function returns the hexadecimal representation of the hash. If the input is empty, the function returns None.

The test section includes a test for a non-empty string and a test for an empty string, both of which confirm the correct operation of the function.