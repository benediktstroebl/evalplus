```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of a given text string. It first checks if the input string is empty or not by using the `strip()` method to remove any whitespace characters at the beginning or end of the string. If the string is empty, the function returns `None` to comply with the problem's request. If the string is not empty, it computes the MD5 hash of the text using the `hashlib.md5()` function, which takes the string as an input and returns the hash as a binary digest. Then, the binary digest is converted into a hexadecimal string using `hexdigest()`, and it is returned as the result. 

To follow the problem's spec, the function handles the edge case of an empty string by returning `None`, and it successfully computes the MD5 hash for any non-empty string input. 

To use the function in the script provided in the original problem text, add the following test case to verify its behavior:
```python
def test_string_to_md5():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
``` 
This test case checks if the function's output corresponds to the known MD5 hash of "Hello world" and verifies that the function returns None for an empty input.