```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Compute the MD5 hash of the given string or return None for an empty input.

    Parameters:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash as a string, or None if the input is empty.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The function `string_to_md5` takes a text string as input and uses the `hashlib.md5()` function to compute the MD5 hash. The `update()` method is then used to update the hash with the contents of the input string, and `hexdigest()` is used to return the hash as a string.

The return value is `None` if the input string is empty, and otherwise, it is the MD5 hash equivalent string. 

This solution complies with the problem statement and corresponds with the given test case.  It also has acceptable performance because it uses a built-in hash function to achieve the MD5 hash.