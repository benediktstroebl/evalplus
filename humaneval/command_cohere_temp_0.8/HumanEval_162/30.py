```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function utilizes the `hashlib` module in Python which provides an implementation of cryptographic hash functions, including the MD5 algorithm. The function calculates the MD5 hash of the input text and returns it as a hexadecimal string.

The specified test case, `string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'`, is designed to validate the accuracy of the function. It compares the MD5 hash of the input string "Hello world" with the known MD5 hash value of "3e25960a79dbc69b674cd4ec67a72c62". 

The function's behavior when an empty string is encountered is defined by the `if not text:` check. In such cases, the function returns `None`, as stated in the problem statement. This is important because MD5 is not considered a secure hash function and should not be used for secure applications. However, it's still useful for simple checks like this. 

**NOTE:** Although MD5 was widely used in the past, it is now considered to be insecure for secure applications. This is due to vulnerabilities that have been discovered in the algorithm, and it is highly recommended that you use more secure hash functions for any sensitive applications. However, MD5 is still useful for simple checks like validating data integrity or for problems like the one posed.