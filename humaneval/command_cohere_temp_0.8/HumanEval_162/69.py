```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8, calculates the hash, and then returns the hexadecimal representation of the hash. If the input string is empty, it returns `None`. This method ensures that the returned hash is always a string. 

The MD5 hash is a 33-character string unique to each input string. MD5 hashing is a standard procedure in cryptography, particularly for password storage or checking. However, due to concerns about MD5's security, it is presently advised to utilize more secure hashing algorithms like SHA-256 for security-sensitive applications.