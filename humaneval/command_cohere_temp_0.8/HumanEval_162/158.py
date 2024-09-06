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
    if not text.strip():
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function string_to_md5 takes a text string as input and returns its MD5 hash. The MD5 hash is a unique string representation of the input text, ensured by the hashlib library. 

If the input is empty, the function returns None, avoiding unnecessary computations and potential errors. The function is self-contained and can be executed independently. It is also formatted with a docstring to provide easy understanding and usage feedback.

Note that MD5 is not considered secure, and you should use more secure hashing functions like SHA-256 for security-sensitive applications.