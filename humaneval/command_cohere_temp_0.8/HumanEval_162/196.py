```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Compute the MD5 hash of the given string or return None for an empty input.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a lowercase hexadecimal string or None for empty input.
    """
    if not text:
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest().lower()
```

The function `string_to_md5` takes a string text as input and returns its MD5 hash as a lowercase hexadecimal string. The MD5 hash is computed using the `hashlib.md5()` function from the hashlib module in Python. The `update()` method is used to feed the input string to the MD5 hashing object, and the `hexdigest()` method returns the hexadecimal representation of the hash.

To handle the special case of an empty input string, the function checks for `not text` at the beginning of the code block. If the input string is empty, the function returns `None`.

This code ensures that the MD5 hash is calculated correctly for non-empty input strings and returns `None` when the input is empty.