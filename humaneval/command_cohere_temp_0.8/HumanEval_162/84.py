```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty by using the `strip()` method to remove any whitespace at the beginning and end of the string, this ensures that leading or trailing whitespaces won't cause the function to return an empty hash. Then if the text is valid, it computes the MD5 hash using the `hashlib.md5()` function, and finally, the hash is converted into a hexadecimal string using `hexdigest()` which is then returned. If the input is empty, the function returns `None`. 

This MD5 hash function provides a reliable and efficient way to verify the integrity of textual data and can be easily integrated into various applications and testing frameworks.