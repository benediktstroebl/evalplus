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

The provided Python function string_to_md5 computes the MD5 hash of a given text string. It utilizes the hashlib module in Python, specifically the md5() function, to generate the hash. The update() method is used to feed the readable text into the hash function, and the hexdigest() method returns the hash in hexadecimal format.

To handle empty input strings, the function includes a condition that returns None if the input is empty. This ensures that the function also satisfies the requirement of yielding None for empty input.

This MD5 hash function is a valuable tool for generating unique hash values for strings, particularly in scenarios where you need a hash function with a fixed length and lower computational cost compared to newer and more secure hash functions. 

It's important to note, however, that MD5 is not suitable for security applications due to its vulnerabilities. This hashing function is primarily suited for simple data integrity checks or cases where a quick and dirty hash is sufficient. 

In summary, the function provides a convenient way to compute the MD5 hash of a string in Python, while handling empty inputs with the appropriate None return value.