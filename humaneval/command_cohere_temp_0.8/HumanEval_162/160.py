```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a string,
    or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains any whitespace using the `strip` method, and if so, it proceeds to calculate the MD5 hash using the `hashlib.md5` method on the encoded version of the text and returns it as a hexadecimal string. If the input is empty or contains only whitespace, it returns `None`. 

This approach ensures that the function handles both non-empty and empty input cases correctly. 

To run the code, you need to have the `hashlib` module available, which typically comes with Python's standard library, so no extra dependencies are required. 

To test this code, you can run it through the provided input test cases. For the given example test case `'Hello world'`, the output should be `'3e25960a79dbc69b674cd4ec67a72c62'`, as indicated in the docstring.