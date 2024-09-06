```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or just contains whitespace with the `if text and text.strip()` syntax. If the condition is met, it computes the MD5 hash using the `hashlib.md5()` function and returns the hexadecimal representation of the hash using `hexdigest()` method. If the input is empty or contains only whitespace, it returns `None`. 

This approach ensures the correct conversion of the input text to its MD5 hash, adhering to the problem statement's requirements.