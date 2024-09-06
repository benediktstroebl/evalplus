```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8, calculates the MD5 hash, and then returns the hexadecimal representation of that hash, adhering to the problem statement. If the input is an empty string, it returns `None`. The function is designed to be self-contained, meaning it does not rely on any external variables or contexts; it encapsulates all the necessary functionality to solve the problem within the function itself.