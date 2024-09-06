```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python function uses the `hashlib` module to generate an MD5 hash. It encodes the input string as UTF-8 bytes and updates the MD5 hash object with the encoded data. Finally, it returns the hexadecimal representation of the MD5 hash. The function also handles the special case where the input string is empty, returning `None` for such inputs.

This solution adheres to the problem statement's requirement of returning `None` for empty input strings, providing a clear and accurate implementation for handling MD5 hashes in Python. 

```python
# Testing the function
text = "Hello world"
expected_result = '3e25960a79dbc69b674cd4ec67a72c62'
result = string_to_md5(text)

if result == expected_result:
    print("Test passed!")
else:
    print("Test failed!")
``` 
The test case provided evaluates the `string_to_md5()` function with the text "Hello world" and compares the result with the expected MD5 hash. Since the result matches the expected hash, it prints "Test passed!" indicating that the function works as intended.  This is a clear and concise way to validate the functionality of the MD5 hash function.