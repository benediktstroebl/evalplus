```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function string_to_md5 computes the MD5 hash of a given text string. It utilizes the hashlib module in Python, specifically the md5() function, to generate the hash. The update() method is used to feed the readable text into the hash function, and the hexdigest() method returns the hash in hexadecimal format.

To handle empty input strings, the function includes a condition that returns None if text is empty. This ensures that the function returns a valid Python object (i.e., None) instead of raising an error or returning an empty string.

This approach enables the function to handle varying input types effectively, providing a reliable solution for calculating MD5 hashes from strings in Python.