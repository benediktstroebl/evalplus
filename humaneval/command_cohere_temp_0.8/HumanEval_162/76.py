```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8, calculates the MD5 hash, and then returns the hexadecimal representation of the hash. If the input string is empty, it returns `None`. This method ensures that the integrity of the text is verified during the MD5 hash generation process. 

To ensure compatibility and standardized hash calculation, the `hashlib` module is utilized, providing a reliable and efficient approach for computing MD5 hashes in Python.

This function effectively handles both non-empty and empty strings, thus fulfilling the problem statement's requirements.