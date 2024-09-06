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

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains any whitespace using the `strip` method to prevent unexpected behavior. Then, it encodes the text and computes the MD5 hash using the `hashlib.md5` function. Finally, the hash is returned as a hexadecimal string.

This code snippet ensures that empty strings are handled correctly and aligns with the problem statement's requirements. It can be used as a self-contained function to solve the given problem and can be readily integrated into larger projects.