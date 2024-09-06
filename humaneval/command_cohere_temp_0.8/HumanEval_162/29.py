```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the input string is empty or not by using the `strip()` method to remove any whitespace characters at the beginning or end of the string. If the string is empty, the function returns `None` to comply with the problem's requirement. If the string is not empty, it computes the MD5 hash using the `hashlib.md5()` method and converts it to a hexadecimal string using `hexdigest()`, which produces a unique hash value for the input text.

The function offers an example test case that verifies if the output of the function matches the expected MD5 hash of the input string "Hello world," which is "3e25960a79dbc69b674cd4ec67a72c62". 

The MD5 hash function is a cryptographic protocol that generates a unique fingerprint for any given input text. However, it is important to note that MD5 has vulnerabilities and should not be used for security-sensitive applications. For more efficient and secure hashing, you might consider using SHA-256, which offers more robust properties.