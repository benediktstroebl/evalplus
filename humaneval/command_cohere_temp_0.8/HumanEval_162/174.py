```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. The function encodes the text to UTF-8 bytes and updates the MD5 hash object with the encoded data. Then, it returns the hexadecimal representation of the final MD5 hash as a string, or None if the input text was empty. 

To verify its behavior against the specified test case, you can run the function with the input `Hello world` and compare the result with the specified MD5 hash string, `3e25960a79dbc69b674cd4ec67a72c62`.