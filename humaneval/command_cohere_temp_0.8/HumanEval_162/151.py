```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function called `string_to_md5` that takes a single argument, `text`, which is of type `str` or `None`. This function calculates the MD5 hash of the input string and returns the resulting hash as a hexadecimal string. If the input string is empty, the function returns `None`.

The function utilizes the `hashlib` module in Python, specifically the `md5()` function to instantiate an MD5 hash object. The `update()` method is then used to feed the input string into the hash object, encoding it first in UTF-8 format. 

The `hexdigest()` method is subsequently employed to return the hexadecimal representation of the calculated hash. This essentially provides the MD5 hash value of the input string, ready for use in various applications such as cryptography, data integrity checks, or basic string identification. 

Overall, the script offers a straightforward approach to converting any given string (or None) into its respective MD5 hash string, with the added reassurance of handling empty strings gracefully by returning None.