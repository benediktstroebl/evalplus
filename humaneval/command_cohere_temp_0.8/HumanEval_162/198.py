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

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is empty or contains only whitespace by using the `strip` method. If it's not empty, the function proceeds to calculate the MD5 hash using the `hashlib.md5` method and then converts it to a hexadecimal string using `hexdigest()`. The resulting hash is then returned if the input is not empty, or None is returned otherwise.  This ensures that the function handles both non-empty and empty strings appropriately, following the requirements of the problem.