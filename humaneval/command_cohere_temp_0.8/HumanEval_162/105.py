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

The `hashlib` module is used here to generate the MD5 hash. The function updates the hash object with the input string encoded in UTF-8 bytes and then returns the hexadecimal digest of the MD5 hash as a string. Also, the function checks for the empty string input and returns 'None' as mentioned in the problem statement.

To run the code and tests, make a copy of this code into a `.py` file and run the file with the command: `python [FILE_NAME].py` in your terminal.