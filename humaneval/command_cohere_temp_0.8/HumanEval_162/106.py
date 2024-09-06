```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8, calculates the MD5 hash, and then returns the hexadecimal representation of that hash. If the input string is empty, the function returns `None`. This method ensures that empty strings don't produce MD5 hashes, adhering to the problem statement's requirement.

The test example provided earlier demonstrates how to verify the function's correctness using the `assert` statement. Comparing the MD5 hash of the `Hello world` string to the expected hash ensures the function produces the desired outcome.