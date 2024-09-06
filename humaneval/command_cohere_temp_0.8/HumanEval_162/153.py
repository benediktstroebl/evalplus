```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string,
    or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

This function uses the `hashlib` module in Python, which provides an interface for common cryptographic hash functions, including the MD5 hash function. It accepts a text string as an input argument and uses the `md5()` method to calculate the MD5 hash of the text. The returned hash is then converted to a string using the `hexdigest()` method.

To check if the input text is an empty string or not, the function uses the `bool()` function along with the `and` and `strip()` methods to ensure the input string is not empty after removing leading and trailing whitespaces, if any.

The `None` value is returned if the input string is empty, indicating the absence of a valid hash value. 

This script provides a self-contained solution to the problem in a concise and functional manner. It can be executed directly to verify its behavior and can be imported and used as a module in other scripts.