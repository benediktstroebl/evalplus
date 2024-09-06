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

The provided Python function uses the `hashlib` module to compute the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains whitespace by using the `strip` method, which removes leading and trailing whitespaces and returns `True` if the string length is greater than zero. If the text is empty, the function returns `None` to conform to the problem's request. Otherwise, it uses the `hashlib.md5()` function to calculate the MD5 hash of the text and encode it as a hexadecimal string using `hexdigest()`.

The tests for the function can be performed by asserting the equality of the returned hash with the expected hash value for a given string.