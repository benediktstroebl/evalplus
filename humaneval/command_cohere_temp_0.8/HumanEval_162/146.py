```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a lowercase hexadecimal string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode('utf-8')).hexdigest().lower()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. The function checks if the input is empty or contains only whitespace before calling the MD5 hash function to ensure efficiency and avoids unnecessary computations. The returned MD5 hash result is then converted to a lowercase hexadecimal string.

To use this function, make sure the `hashlib` module is installed, or import the module as needed. 

**Note**: MD5 is no longer considered secure due to vulnerabilities, so it's advisable to use more secure hashing algorithms like SHA-256 for security-sensitive applications.