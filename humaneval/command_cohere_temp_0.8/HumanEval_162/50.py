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

The provided solution leverages the `hashlib` module in Python, specifically the `md5()` function to encrypt the input string. The function `update()` allows the encryption of the string and the `hexdigest()` method provides the encrypted string in hexadecimal format. The output of the example sentence provided in the problem declaration would be:
```bash
'3e25960a79dbc69b674cd4ec67a72c62'
```