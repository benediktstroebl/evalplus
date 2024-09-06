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

The provided Python function uses the `hashlib` module to compute the MD5 hash of the input `text`. It first checks if the `text` is not empty or contains any whitespace using the `strip` method, and then proceeds to calculate the hash. The resulting hash is returned as a hexadecimal string. If the input is empty or contains only whitespace, the function returns `None`. 

To showcase the behavior of the function, you can use the following test:
```python
test_string = 'Hello world'

# Test the string_to_md5 function
assert string_to_md5(test_string) == '3e25960a79dbc69b674cd4ec67a72c62'
```

The expected result for the test case is `3e25960a79dbc69b674cd4ec67a72c62`, which is the MD5 hash of the string "Hello world".