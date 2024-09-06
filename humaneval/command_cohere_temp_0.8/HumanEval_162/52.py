```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the input string is empty or not using the `strip()` method to remove any leading or trailing whitespaces. If the string is empty, the function returns `None` to comply with the problem's request for handling empty input. If the string is not empty, it computes the MD5 hash using the `hashlib.md5()` function and the `update()` method to update the hash object with the encoded input string in UTF-8 format. Finally, the function returns the hexadecimal representation of the calculated MD5 hash using the `hexdigest()` method. 

This code guarantees that the MD5 hash is accurately computed for non-empty texts and handles empty inputs as specified in the problem statement.