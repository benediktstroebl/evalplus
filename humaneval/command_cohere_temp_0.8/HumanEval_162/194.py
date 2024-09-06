```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This function utilizes the `hashlib` module in Python which provides an interface to many different secure hash and message digest algorithms. In this case, we use the MD5 algorithm to hash the input text. The function also includes type-hints to indicate that the function takes a string (`text`) as an argument and returns either a string or None, reflecting the specifications of the problem. 

To test this function, you can use the following script:
```python
import string_to_md5

# Test Case: Non-empty string
text = "Hello world"
result = string_to_md5.string_to_md5(text)
print(result)  # This should print the expected result which is '3e25960a79dbc69b674cd4ec67a72c62'

# Test Case: Empty string
text = ""
result = string_to_md5.string_to_md5(text)
print(result)  # This should print None
```

This provides a basic test of the function, checking for the correct output on both a non-empty and empty string. 
For more thorough testing of this function, consider testing it with a wider range of input texts, including texts of different lengths, with different characters (e.g., digits, special characters, etc.), and even invalid inputs (e.g., non-string inputs) to ensure its robustness against various scenarios. 
This will help validate the function's behavior against potential edge cases and its handling of invalid inputs.