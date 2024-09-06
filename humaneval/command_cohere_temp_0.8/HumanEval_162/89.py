```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It's a straightforward implementation that fulfills the problem's requirement. Note that MD5 is no longer considered secure due to vulnerabilities, so it's essential to use more secure hashing algorithms like SHA-256 for security-sensitive applications.