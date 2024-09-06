```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string,
    or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains any whitespace using the `stripped` method, which ensures that empty strings are also considered valid input.  The function then encodes the text and computes the MD5 hash using the `hashlib.md5()` function, returning the hash as a hexadecimal string. If the input is empty or contains only whitespace, the function returns `None`. 

This code provides a convenient way of encoding text and generating MD5 hashes in Python while handling edge cases gracefully.