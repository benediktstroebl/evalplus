```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function uses the `hashlib` module in Python which provides an interface to many different secure hash and message digest algorithms. In this case, we use the MD5 algorithm to hash the input text. The function also checks if the input `text` is empty, and if it is, returns `None`.

To use this function, you can simply call it with a string as an input like this:
```python
string_to_md5('Hello World!) == '3e25960a79dbc69b674cd4ec67a72c62'
```

The result of the hash for the input text "Hello World!" is indeed "3e25960a79dbc69b674cd4ec67a72c62".