```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It first checks if the input `text` is empty. If empty, it returns `None` because an MD5 hash of an empty string is technically undefined in cryptography. If the text is not empty, it computes the MD5 hash using the `hashlib.md5()` function, encodes the text to bytes using UTF-8 encoding, and updates the hash object with the encoded text. Finally, it returns the hexadecimal representation of the computed MD5 hash using the `hexdigest()` method. 

This code ensures that it handles the case of an empty input string appropriately and conforms to the test requirement provided.