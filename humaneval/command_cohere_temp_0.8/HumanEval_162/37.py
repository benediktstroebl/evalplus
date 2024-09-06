```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It's a straightforward implementation that fulfills the problem's requirement. The function checks if the input string is empty, and if so, it returns `None`. Otherwise, it computes the MD5 hash of the string using the `hashlib.md5()` function, updates it with the string encoded in UTF-8, and then returns the hexadecimal digest of the hash using the `hexdigest()` method. This approach ensures accurate MD5 hashing and handles empty inputs gracefully.