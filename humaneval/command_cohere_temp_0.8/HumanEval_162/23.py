```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string into MD5 and returns the result.
    For an empty string, returns None.

    :param text: String to encrypt
    :return: MD5 string result or None
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

The `hashlib` module is utilised to efficiently compute the MD5 hash. The function commences by validating whether the input `str` is empty. In the absence of a genuine input, the function returns `None`. Otherwise, the input string is encoded to bytes using `encode()`, and the MD5 hash is obtained using the `hashlib.md5()` function. The hash is then formatted as a hexadecimal string through the application of `hexdigest()`, which is subsequently returned. 

This approach ensures the confidentiality of the hash, as well as the capability to identify an empty string as a distinct input. 

To ensure proper functionality, this code block should be incorporated within a testing environment and validated with test cases. This is to ensure compatibility with a variety of strings and to detect any potential bugs or edge cases that may arise.