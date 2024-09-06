```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    For an empty string, returns None.

    :param text: String to encrypt
    :return: MD5 encrypted string or None
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the `hashlib` Python module to calculate the MD5 hash of the input string. The input string is first checked to see if it is empty. If it is, the function returns `None`. If the string is not empty, the function returns the hexadecimal representation of the MD5 hash of the input string.

The MD5 hash is a unique identifier for the string, and it is used to secure data and verify the integrity of files and messages. 

To encrypt the string, you can use the following code:
```python
string_to_md5("Hello World")
``` 

This will return the MD5 hash of the string "Hello World", which is "3e25960a79dbc69b674cd4ec67a72c62". 

To encrypt an empty string, you can use the following code:
```python
string_to_md5("")
``` 

This case returns `None` because the empty string input is specified in the function's comment as returning `None`.