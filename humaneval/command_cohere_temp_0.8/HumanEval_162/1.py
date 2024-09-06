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

The provided Python function uses the `hashlib` module to compute the MD5 hash of the input `text`. The function checks if the input is empty or contains only whitespace before calling the MD5 hash function to ensure it doesn't attempt to calculate the hash of an empty string. The result is then returned as a hexadecimal string representation of the hash, or `None` if the input is empty.