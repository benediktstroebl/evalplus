```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` module to generate the MD5 hash. It first checks if the input string is empty, and if it is, returns None. If the input is not empty, it returns the MD5 hash of the input string.