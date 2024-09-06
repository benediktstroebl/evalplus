```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings correctly.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text and text.strip():
        # Add the hashlib library to create an MD5 hash
        md5 = hashlib.md5()
        # Encrypt the string and get the hash
        text = md5.hexdigest(text.encode()).decode()
    else:
        text = None
    return text
```

The provided Python function string_to_md5 takes a text string as input and returns its MD5 hash. This hash is a unique value that represents the encrypted text. The MD5 hash is created using the hashlib library and the hexdigest method.

To handle empty strings or spaces correctly, the function checks if the input string is empty or contains only spaces (i.e., text is None or not blank), then it returns None. Otherwise, the function proceeds to encrypt the text and return the MD5 hash.

The code is designed to be self-contained and does not rely on external variables, so it can be executed directly as a standalone script.