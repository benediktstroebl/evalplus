```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the input string is empty, and if so, returns `None` to comply with the problem's request. Otherwise, it computes the MD5 hash using the `hashlib.md5()` function, updating it with the text encoded in UTF-8. Finally, the hexadecimal representation of the hash is returned using the `hexdigest()` method. 

To verify the correctness of the function, you can compare its output with the provided test case's expected result.