```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function string_to_md5 computes the MD5 hash of a given text string. It utilizes the hashlib module in Python, specifically the md5 hash object, to generate the hash. The text is first encoded as UTF-8 and then passed to the md5 object using the update method. Finally, the hexdigest method is used to retrieve the hexadecimal representation of the hash, which is then returned.

In the initial implementation, the function checks if the input text is empty. If empty, it returns None, as stipulated in the problem statement. This ensures that the function correctly handles empty inputs. 

This function provides a straightforward way to obtain the MD5 hash of a string in Python, and it can be used for various purposes, including verifying file integrity, checking password validity, or ensuring data integrity in communications or storage.