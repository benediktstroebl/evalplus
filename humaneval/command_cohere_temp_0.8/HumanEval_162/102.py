```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function called `string_to_md5` that takes a single argument `text`, which is of type `str` and returns a `str` or `None` based on the following logic:
- If the `text` is empty, it returns `None`.
- Otherwise, it proceeds to compute the MD5 hash of the provided string using the `hashlib.md5()` function and the UTF-8 encoding.
- Finally, it returns the hexadecimal representation of the computed MD5 hash using the `hexdigest()` method of the `md5` hash object.

This script ensures that when an empty string is provided, it returns `None` due to the conditional check. And for any non-empty string input, it computes and returns the corresponding MD5 hash as a hexadecimal string.