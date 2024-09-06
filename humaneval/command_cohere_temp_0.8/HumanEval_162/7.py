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

The provided Python function uses the `hashlib` module to generate the MD5 hash. It first checks if the input string is empty or not using `not text.strip()` to avoid errors arising from empty strings. If the string is not empty, it computes the MD5 hash using the `update()` method to encode the input string in UTF-8 and calculates the hash. 

The MD5 hash is then returned as a hexadecimal string using the `hexdigest()` method. If the input string is empty, the function returns None. 

This solution covers the given test case and also handles any potential empty string inputs effectively. 
The solution could be improved by adding a docstring and typing for the function as follows:
```python
def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.
    
    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if not text:  # using this notation instead of `if not text.strip()`
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest()
``` 
This adds some clarity to the code and provides better understanding for users who might be reading the code.