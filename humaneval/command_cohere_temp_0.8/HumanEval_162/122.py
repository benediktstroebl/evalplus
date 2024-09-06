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

The `hashlib` module is used here to generate the MD5 hash. The function updates the hash object with the input string encoded in UTF-8, then returns the hexadecimal digest of the hash as a string. If the input is an empty string, the function returns `None`.