```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It's important to note that while MD5 was widely used for checksums and authentication in the past, its security vulnerabilities have been exposed, and it is not recommended for secure applications. For more sensitive use cases, consider using a secure hashing algorithm like SHA-256 instead.

The function goes through the following steps:
1. The `hashlib.md5()` function is used to instantiate an MD5 hash object.
2. The `update()` method is applied to the MD5 object, where it takes the input text, encodes it as UTF-8, and feeds it into the hash object.
3. Finally, the `hexdigest()` method is used to return the hexadecimal representation of the calculated MD5 hash, which is then returned as the result of the function.

This method efficiently computes the MD5 hash of the given text and returns it as a hexadecimal string, thereby fulfilling the problem statement.