```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to compute the MD5 hash of the input `text`. The MD5 hash is a unique fingerprint of the input text. 

The function checks if the input `text` is not empty by using the `strip` method to remove any leading or trailing whitespaces and then checks if it's empty. The returned MD5 hash is then represented as a hexadecimal string using the `hexdigest` method. 

You can verify the correct behavior of the function by testing it with the provided test case:
```python
test_string = 'Hello world'
expected_result = '3e25960a79dbc69b674cd4ec67a72c62'

assert string_to_md5(test_string) == expected_result
```

The function also handles empty input correctly, returning `None` for empty strings. 

Please note that MD5 is no longer considered a secure hashing algorithm due to its vulnerabilities. For security-sensitive applications, it's recommended to use more secure hash functions like SHA-256 or SHA-3.