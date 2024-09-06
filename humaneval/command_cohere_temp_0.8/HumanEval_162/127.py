```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8 to ensure compatibility with the hash function. The resulting hash is then converted to a hexadecimal string using the `hexdigest()` method.

To verify the correctness of the function, we can compare the generated MD5 hash with the expected hash value. The expected value provided in the example is "3e25960a79dbc69b674cd4ec67a72c62", which corresponds to the MD5 hash of the string "Hello world".

By incorporating this function, developers can easily generate MD5 hashes for any given non-empty string input and handle empty strings gracefully by returning `None`. This can be particularly useful for various security-related tasks, such as password validation, data authentication, and integrity checks.