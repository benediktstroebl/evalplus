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

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains whitespace by using the `str.strip()` method to remove leading and trailing whitespaces and then checks if it's not empty. If the condition is met, it proceeds to calculate the MD5 hash using the `hashlib.md5()` method, which takes the input text encoded as bytes (`text.encode()`), and then returns the hexadecimal representation of the hash using `hexdigest()` method. 

The reason for encoding the text to bytes is that the MD5 hash function works on binary data, and `hashlib` expects binary inputs. 

If the input text is empty or contains only whitespace, the function returns `None`, as per the problem statement. 

This function efficiently and accurately solves the task of converting a string to its MD5 hash.