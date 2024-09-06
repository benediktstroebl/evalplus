```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It first checks if the input `text` is empty. If empty, it returns `None` because an MD5 hash of an empty string is also empty, and None represents the absence of a hash value. If the text is not empty, it computes the MD5 hash by creating an instance of the MD5 hash object and updating it with the encoded UTF-8 version of the input string using the `update()` method. Finally, it returns the hexadecimal representation of the computed MD5 hash using the `hexdigest()` method. 

The function is designed to follow best practices by handling empty input strings gracefully and ensuring the correct encoding of the input string to maintain compatibility with different text encodings.