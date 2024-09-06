```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python function uses the `hashlib` module to generate an MD5 hash. The function will return `None` if the input is an empty string. The MD5 hash is then returned as a string. This function ensures that the input is properly encoded in UTF-8 to allow for proper hashing. 
The test example provided can be tested with the following markdown:
```python
>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
True
``` 
This generates the correct hash for the given string. 

If an empty string is inputted:
```python
>>> string_to_md5('')
None
``` 
This is the correct output for an empty string input.