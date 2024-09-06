```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8 bytes and updates the MD5 hash object with the encoded data. Finally, it returns the hexadecimal representation of the MD5 hash. The function also handles the special case where the input string is empty, returning `None` instead of the MD5 hash to align with the problem statement's requirements.

For validation, you can compare the output of the function with the known MD5 hash values for various strings using Python's built-in `assert` statement or the `unittest` module for more comprehensive testing.