```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to MD5 and returns the result.
    For an empty string, returns None.
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

The `hashlib` module is utilized to directly hash the text using the `md5` algorithm. The function warrants that empty strings return `None` and utilizes the `encode()` method to make sure that the text is hashed correctly, notably if the text includes non-ASCII characters. 

Here is an example usage of the function:
```python
string_to_md5("Hello World!")
'3e25960a79dbc69b674cd4ec67a72c62'

string_to_md5("")
None
```

The example usage demonstrates the function's behavior when handling a regular text and an empty one. 

Note that the `hashlib` module is part of Python's standard library since version 3.0. In case you're using an earlier version, you may need to activate it by typing `import hashlib` in your script's main body.