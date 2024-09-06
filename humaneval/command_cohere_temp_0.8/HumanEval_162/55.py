```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text and text.strip():
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the `text` parameter is provided, and if it's not empty or containing only whitespace with the `trim()` method. If the condition is met, it computes the hash using the `md5()` function from the `hashlib` module and returns the hexadecimal representation of the hash using the `hexdigest()` method. If the input is empty, the function returns `None`.

This function effectively balances simplicity and efficiency, making it a robust solution for converting text into MD5 hashes in Python while returning `None` for empty inputs to handle edge cases gracefully.