```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Compute the MD5 hash of the given string or return None for an empty input.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a lowercase hexadecimal string or None for empty input.
    """
    if not text:
        return None
    
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    
    return md5.hexdigest().lower()
```

This script imports the `hashlib` module, which is normally included in Python's standard library. If `hashlib` is not available, you may need to install it separately with the command `pip install hashlib`.

The `string_to_md5` function takes a string text as input and returns its MD5 hash as a lowercase hexadecimal string, or None if the input is empty. The function first checks if the input string is empty using the `if not text:` condition. If the string is empty, it returns `None`. Otherwise, it proceeds to compute the MD5 hash using the `hashlib.md5()` function. This function takes an optional string as an input and returns an object that can compute the MD5 hash of the given string. 

The `md5.update(text.encode('utf-8'))` method takes the input string and encodes it as UTF-8 bytes, which is necessary for the MD5 computation. Finally, the function returns the MD5 hash as a lowercase hexadecimal string using the `md5.hexdigest()` method. 

The tests for this function are also provided in the same script, right below the function definition. These tests check if the function behaves as expected on various inputs, including non-empty strings and empty strings. The test scheme is as follows:
```python
# Test on a non-empty string
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

# Test on an empty string
assert string_to_md5('') is None
```

You can add more tests to this block to test the function on various other inputs as per the problem statement.