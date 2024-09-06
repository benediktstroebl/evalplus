```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the hashlib library in Python to compute the MD5 hash of the input text. The function encodes the text in UTF-8 encoding before computing the hash value. The resulting hash value is returned in hexadecimal format.

To verify the correctness of the function, you can use the following test:
```python
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
```

This test uses the example string from the problem statement and compares the computed hash value against the expected value. 

Note, MD5 is no longer considered a secure hashing algorithm, and it is not recommended for security-sensitive applications. However, it is still widely used for simple integrity checks or when stronger algorithms are not required.