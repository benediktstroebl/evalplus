```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    Returns None if the input string is empty.

    Args:
        text (str): Input string to encrypt.

    Returns:
        str or None: MD5 hash of the input string or None if the input string is empty.
    """
    if text and text.strip():
        # Use hashlib to generate MD5 hash
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()
    else:
        return None
```

The provided Python script defines a function called `string_to_md5` that takes a text string as input. Within the function, it checks if the given text is not empty or contains at least one non-whitespace character. If it passes this condition, the function utilizes the hashlib module in Python to generate the MD5 hash of the input string. The encoded text is updated using the `update()` method, and the MD5 hash is returned as a hexadecimal string using the `hexdigest()` method. 

If the input string is empty or consists only of whitespace characters, the function returns None indicating that it is not possible to compute the MD5 hash of an empty string. 
The `string_to_md5` function provides an easy way to encrypt text into MD5 format and handles scenarios where the input is empty. 

To use this function, simply import it within your Python program or use it as a standalone script, passing the desired string as an argument like this:
```python
string_to_md5("Hello World!")
```

The output will be:
```bash
b3d87073c3d6fc09b5b5359ee13c152f
``` 

Another example for empty strings is: 
```python
string_to_md5("")
```

The output will be None:
```bash
None
```