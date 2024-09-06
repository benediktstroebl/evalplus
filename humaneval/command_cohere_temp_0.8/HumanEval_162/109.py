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

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains any whitespace using the `strip` method, and then proceeds to calculate the hash. The resulting hash is returned as a hexadecimal string. If the input is empty or contains only whitespace, the function returns `None`. 

To avoid any confusion, it's worth mentioning that MD5 is no longer considered secure due to vulnerabilities. Using SHA-256 or another more secure hashing algorithm is recommended for better security when possible.