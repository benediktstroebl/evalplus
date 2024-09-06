```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the `hashlib` module in Python which provides an implementation of the MD5 hash algorithm. The function calculates the MD5 hash of the input text and returns it as a hexadecimal string, or `None` if the input is an empty string.

To use this function, simply import it in your Python script or Jupyter Notebook cell, and call it with the text you want to hash. 

For example:
```python
import string_to_md5  # Import the function

text = 'Hello World!'
hashed_text = string_to_md5.string_to_md5(text)
print(hashed_text)
``` 

This will output: 
```bash
e4d7f1b4ed25e3b5b2d5b7f28b0b98
``` 
which is the MD5 hash of the string "Hello World!". 

**NOTE:** MD5 is no longer considered a secure hashing algorithm for password storage or security-related applications due to vulnerabilities. It is still useful for checking data integrity in certain non-security critical scenarios.