```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the hashlib library in Python to compute the MD5 hash of the input string. The function encodes the string to UTF-8 format before calculating the hash value. The resulting hash value is then returned in hexadecimal format.

The function checks for an empty input string and returns None if it is empty. This is in line with the problem statement that asks to return None if the input string is empty.

**NOTE**: MD5 is a cryptographic hash function that has been found to have security vulnerabilities, hence it is recommended to use more secure hash functions for sensitive applications. This function is provided for educational purposes solely and accomplishes the given task effectively. 

The problem statement includes a test case ('Hello world') and the provided code returns the expected result ('3e25960a79dbc69b674cd4ec67a72c62').