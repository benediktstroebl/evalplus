```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the input string is empty, and if so, returns None because an MD5 hash of an empty string is also empty. If the text is not empty, it computes the MD5 hash using the `hashlib.md5()` function and the `update()` method to encode the text into bytes using UTF-8 encoding and update the hash object with the data. Finally, it returns the hexadecimal representation of the computed MD5 hash using the `hexdigest()` method. 

This ensures that the function handles the edge case of an empty input string correctly, and provides a straightforward solution for calculating the MD5 hash for any non-empty string input.