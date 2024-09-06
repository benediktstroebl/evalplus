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
```

The `update()` method of the `hashlib.md5()` object takes a string (or bytes) and encodes it as 'utf-8'. The `hexdigest()` method returns the hexadecimal representation of the hash. 

An example usage of the function is as follows:
```python
string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
```

This would return the string `3e25960a79dbc69b674cd4ec67a72c62`, the MD5 hash value for the string "Hello world".