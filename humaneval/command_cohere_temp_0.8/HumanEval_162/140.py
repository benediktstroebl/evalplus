```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the hashlib library in Python to calculate the MD5 hash of the input text. The function encodes the input string to UTF-8 format before creating the MD5 hash. The resulting hash is then converted to a hexadecimal string using the hexdigest() method of the MD5 object.

If the input is an empty string, the function returns None, as per the prompt's instructions.

To use this function in your code, simply import it and call it with your desired input text:
```python
import string_to_md5  # Assuming you've imported the function from a file called "string_to_md5.py"

result = string_to_md5.string_to_md5("Hello, World!")
print(result)  # This will print the MD5 hash of "Hello, World!" to the console
```

Note that MD5 is no longer considered a secure hashing algorithm for important cryptographic purposes, as it has vulnerabilities. However, it's still acceptable for simple tasks like checking for string equality or producing unique identifiers for non-sensitive data.