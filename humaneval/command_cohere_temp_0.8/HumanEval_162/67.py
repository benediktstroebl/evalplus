```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings correctly.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a string or None if the input is empty.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` Python module to calculate the MD5 hash. It first checks if the input string is empty, and if it is, returns None. If the input is not empty, it calculates the MD5 hash of the input string and returns it as a string.

The MD5 hash function is not considered secure, and you should use more secure functions like SHA-256 for hashing if security is a concern. If you're concerned with password hashing, use libraries like `bcrypt` or `argon2` specifically designed for password hashing. 

I hope this helps. Let me know if you need anything else!