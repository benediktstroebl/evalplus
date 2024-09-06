```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if not text.strip():
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest()
```

The provided solution leverages the `hashlib` module available in the Python standard library, which provides an interface to many common cryptographic hash and message digest algorithms. Specifically, it uses the `md5()` function to instantiate an MD5 hash object. The `update()` method is then used to feed the input string into the hash object, converting it to bytes using UTF-8 encoding. Finally, the `hexdigest()` method returns the hexadecimal representation of the hash, which is the MD5 sum of the input string.

To address the concern of empty strings, the function checks if the input string is empty or contains only whitespace characters using the `not text.strip()` condition. The `strip()` method removes any leading and trailing whitespaces from the string. If the string is empty after stripping, the function returns None as stated in the problem statement.