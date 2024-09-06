```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the string text as a lowercase hexadecimal string.
    If the input is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest().lower()
```

The function uses the `hashlib` module in Python which provides an implementation of cryptographic hash functions, including the MD5 hash algorithm. The function uses the MD5 hash algorithm to hash the input text and because the hashing operation is non-reversible, the original text cannot be recovered from the MD5 hash. 

To hash the text, the function makes use of the `update()` method to update the hash object with the text and then calls the `hexdigest()` method to obtain the hexadecimal representation of the hash which is then converted to lowercase to return as the result.