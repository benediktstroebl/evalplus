```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function takes a string text as input and returns its MD5 hash as a string, or None if the input string is empty. The function updates the MD5 hash object with the encoded input string and then returns the hexadecimal representation of the hash.

The tests for this function can be exercised as follows:
```python
# Test Case: Valid Input
text = "Hello World!"
expected_result = "3e25960a79dbc69b674cd4ec67a72c62"
result = string_to_md5(text)
assert result == expected_result

# Test Case: Empty String Input
text = ""
expected_result = None
result = string_to_md5(text)
assert result == expected_result
```

This test suite verifies the correct operation of the `string_to_md5` function for both valid and empty input strings. 

It's important to note that the MD5 hash function has vulnerabilities and is considered insecure for certain applications. Hash functions like SHA-256 are recommended for higher security levels. However, for the purpose of this exercise, MD5 is used to match the specified problem statement.