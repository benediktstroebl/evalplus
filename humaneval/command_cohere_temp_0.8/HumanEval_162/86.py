```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function called `string_to_md5` that takes a string text as input. Within the function, it checks if the input text is empty using the `if not text:` condition. If the text is empty, the function returns `None`, indicating that the MD5 hash cannot be calculated for an empty input. Otherwise, it proceeds to compute the MD5 hash of the input text. 

The `hashlib.md5()` function is imported from the `hashlib` module and used to create an instance of the MD5 hash algorithm. The `update()` method is then applied to the MD5 object, taking the `utf-8` encoded version of the input text. This step ensures that the text is correctly encoded before being hashed. Finally, the `hexdigest()` method is used to retrieve the hexadecimal representation of the computed MD5 hash, which is then returned as the result of the function. 

The function's annotation `str or None` specifies that the return value is either a string (the MD5 hash) or `None` (if the input is empty). This type annotation is important to indicate the potential None return value and the fact that the return value is either a string or null. 

When calling the function with the input `'Hello world'`, the expected MD5 hash `3e25960a79dbc69b674cd4ec67a72c62` is returned, confirming the correctness of the implementation. 

This MD5 hash function can be used for various purposes, including checking the integrity of files, verifying the authenticity of messages, or as a simple fingerprint for text data. 

Overall, the provided code offers a practical and efficient way to generate MD5 hashes directly in Python, aiding in various security- and data integrity-related tasks. 

**NOTE:** It is important to note that MD5 is no longer considered a secure hashing algorithm for cryptographic purposes due to vulnerabilities. It is recommended to use more secure hashing algorithms like SHA-256 for cryptographic uses. However, MD5 is still widely used for non-cryptographic purposes, such as checksum validation or data fingerprinting.