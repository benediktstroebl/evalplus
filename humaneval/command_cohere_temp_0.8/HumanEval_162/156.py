```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function takes a string text as an argument and returns its MD5 hash as a string, or None if the input is an empty string. 

The function employs the `hashlib.md5()` function to create an MD5 hash object, and the `update()` method to feed the text into the hash object. Finally, the `hexdigest()` method is used to return the hash in hexadecimal format. 

The example test case is provided to demonstrate the correct behavior of the function. It checks if the MD5 hash of the string "Hello world" corresponds to the expected value "3e25960a79dbc69b674cd4ec67a72c62". 

You can further verify the correctness of the function by calling it with different strings and comparing the results with the expected MD5 hashes.