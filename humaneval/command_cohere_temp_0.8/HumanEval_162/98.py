```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function `string_to_md5` that takes a string text as input and returns its MD5 hash as a lowercase hexadecimal string. The function utilizes the `hashlib` module to compute the MD5 hash of the input text, and ensures that empty strings are handled correctly by returning `None`. 

To retrieve the MD5 hash, the function first encodes the input string using UTF-8 encoding, then computes the hash using the `hashlib.md5()` function. Finally, the hexadecimal representation of the hash is obtained through the `hexdigest()` method of the MD5 object. 

This code demonstrates how to hash text using the MD5 algorithm to get a unique fingerprint for strings, and the output of the function can be compared to the provided test case to verify correctness. 

Usage example:
```python
# Example usage
text = "Hello World!"
result = string_to_md5(text)
print(result)
```