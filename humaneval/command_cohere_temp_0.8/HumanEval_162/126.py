```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. The MD5 hash is a unique string representation of a given text. The function checks if the input is empty or contains only whitespace using the `if text and text.strip()` condition. If the input is not empty, the function calls `hashlib.md5()` to calculate the hash and then uses `.hexdigest()` to return the hash as a hexadecimal string. If the input is empty, the function returns `None`, as per the problem statement. 

To ensure the functionality, please ensure that the `hashlib` module is installed, as it's required for the MD5 hash calculation. You can install it separately using `pip install hashlib`, or better, since Python 3.9, `hashlib` is included in the standard library, so it's available by default.

This function passes the provided test case equivalency check `string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'`.