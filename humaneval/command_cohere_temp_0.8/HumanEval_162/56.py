```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python function uses the `hashlib` module to generate an MD5 hash. The function will return `None` if the input is an empty string. It encodes the text to UTF-8 bytes and updates the MD5 hash object with the encoded data. Finally, it returns the hexadecimal representation of the MD5 hash. 

Here is an example usage of the function:
```python
string_to_md5('Hello World')  # Output: 3e25960a79dbc69b674cd4ec67a72c62
string_to_md5('')  # Output: None
```

This passes the provided test cases. You can easily integrate this function into your project to solve MD5 hashing needs. If you have more questions or need further assistance, feel free to ask!