```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the `hashlib` module in Python which provides an implementation of the MD5 hash algorithm. The function calculates the MD5 hash of the input text and then returns the hexadecimal representation of the hash. If the input is an empty string, the function returns `None`.

To verify the correct behavior of the function, let's consider an example where we compute the MD5 hash of the string "Hello World":
```python
>>> string_to_md5('Hello world')
'3e25960a79dbc69b674cd4ec67a72c62'
```

Moreover, if we input an empty string, the function returns `None`:
```python
>>> string_to_md5('' )
None
``` 

The output was `None` because the empty string was the input and according to the function's specification, it returns `None` in this case.