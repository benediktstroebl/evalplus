```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python function uses the `hashlib` module to generate an MD5 hash. The function will return `None` if the input is an empty string. The MD5 hash is then converted to a hexadecimal string using `hexdigest()`. 

The example test case included in the problem statement asserts that the MD5 hash of the string "Hello world" is "3e25960a79dbc69b674cd4ec67a72c62". 

Would you like to know more about MD5 hashes, or how to solve this problem using a different language? Feel free to ask for clarification on any of the steps taken to solve this problem, as well!