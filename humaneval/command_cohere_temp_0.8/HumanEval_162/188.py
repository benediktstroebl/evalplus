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

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It first checks if the input `text` is empty, and if so, returns `None` to align with the problem's statement. Otherwise, it computes the MD5 hash using the `hashlib.md5()` function, updating it with the encoded representation of the input string in UTF-8 encoding using the `update()` method, and finally, returns the hexadecimal representation of the computed hash using the `hexdigest()` method. 

This function effectively hashes non-empty text inputs and produces a unique MD5 hash string representing those values.