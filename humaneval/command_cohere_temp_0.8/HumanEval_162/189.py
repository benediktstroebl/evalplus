```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if not text.strip():
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` module in Python which provides an MD5 hash algorithm implementation. It accepts a string input and efficiently computes its MD5 hash, representing it as a hexadecimal string. The function also includes a check for empty strings or strings with only whitespace, which returns `None` to accommodate the specified test case and handle edge cases.