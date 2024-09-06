```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the hexadecimal representation of the hash.
    Returns None if the input is an empty string.
    """
    if text and text != "":
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to generate an MD5 hash for any given non-empty text. The MD5 hash is a 128-bit value that serves as a unique representation of the input text, suitable for authentication purposes or as a quick way to verify the integrity of data. The function returns `None` if the input is empty, in alignment with the problem's request.