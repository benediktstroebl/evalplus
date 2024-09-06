```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

The provided Python script defines a function `string_to_md5` that takes a string text as input. It utilizes the hashlib module in Python which provides APIs for working with various cryptographic hash functions. In this case, the function uses the MD5 hashing algorithm.

If the input text is empty, the function returns None, adhering to the problem's requirement that empty strings should result in None. This is checked using Python's stringent typing system where a variable is explicitly typed, making it possible to catch such conditions.

When text is not empty, the function computes the MD5 hash of the text and returns the hexadecimal representation of the hash. The text is first encoded to UTF-8, which is a standard Unicode encoding, before being updated through the `update()` method of the MD5 object. The `update()` method takes an object (in this case, the encoded text) and updates the hash object with the object's data. 

Finally, the `hexdigest()` method of the MD5 object returns the hexadecimal representation of the computed hash value, which is then returned by the function. 

The function's documentation includes a test case to verify its correctness. This test case checks if the function, when provided with the text "Hello world", returns the expected MD5 hash, "3e25960a79dbc69b674cd4ec67a72c62". The equality operator "==" in Python compares two strings for equality, and since it doesn't provide a boolean output when given unequal strings in this context, it's implicitly True for unequal strings and implicitly False for equal ones. Hence, there's no need to use "== True" as it's implicitly True if the strings are equal.