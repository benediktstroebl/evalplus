```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.
        
    Returns:
        str or None: MD5 hash if text is not empty, otherwise None.
    """
    if not text:
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The function uses the `hashlib` module in Python which implements a general interface to many different secure hash and message digest algorithms. In this case, the MD5 algorithm is used. The MD5 hash is known to be insecure for certain applications, but it still serves well for basic integrity checks, like checking if an input string is empty or not.

The function first checks if the input string is empty. If empty, it returns `None`. Otherwise, it encodes the string to bytes using UTF-8 encoding, calculates the MD5 hash, and then converts this hash back to a string to return to the caller.