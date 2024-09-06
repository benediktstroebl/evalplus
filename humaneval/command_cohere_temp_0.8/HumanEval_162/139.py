```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the `text` argument is provided, and if it's not empty or contains trailing and leading spaces by using the `strip()` method. If the argument satisfies these conditions, it computes the MD5 hash of the text and returns it as a hexadecimal string. Otherwise, if the argument is empty or contains only spaces, the function returns `None`.  This hash function is widely used in various applications, such as cryptography, data integrity checks, and password storage. 

This Python script guarantees that the expected MD5 hash values are generated for the specified test cases and returns `None` for an empty input. 
Remember, MD5 is no longer considered secure due to its vulnerabilities, including collision and fingerprinting attacks. It's advised to use more secure hashing algorithms like SHA-256 for security-related applications.