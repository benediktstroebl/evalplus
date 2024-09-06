```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given string. It encodes the text to UTF-8 format before calculating the hash using the `update()` method. The resulting hash is then converted to a hexadecimal string using the `hexdigest()` method and returned. If the input text is empty, the function returns `None`. 

To install the `hashlib` module, you need to run `pip install hashlib` on the command line.

This approach ensures a secure way to generate MD5 hashes, providing a more reliable solution than traditional methods that might involve ad-hoc regex replacements or weaker hash calculations.