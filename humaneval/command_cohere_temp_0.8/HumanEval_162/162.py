```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the input text as a lowercase hexadecimal string, or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None
```

This function utilizes the `hashlib` module to compute the MD5 hash of the input text. The input text is first checked to see if it is empty or not. If it is empty, the function returns `None`. If the text is not empty, the function uses the `hashlib.md5()` function to generate the MD5 hash of the text and then uses the `hexdigest()` method to return the hexadecimal representation of the hash. 

The tests for this function should check both the validity of the hash for various inputs and the behavior of the function when an empty string is passed in. 

Would you like to create these tests together?
```python
# Test the string_to_md5 function
def test_string_to_md5():
    # Test with a non-empty string
    assert string_to_md5("Hello World!") == "3e25960a79dbc69b674cd4ec67a72c62"
    
    # Test with an empty string
    assert string_to_md5("") is None
```

This is an example of how tests could be created for the `string_to_md5` function to verify the output against the expected MD5 hash values for both empty and non-empty strings. 

**Note**: MD5 hashes are no longer considered secure and should not be used for security-related purposes. This code demonstrates the problem using MD5 for educational purposes only. For security-related applications, consider using a more secure hashing algorithm like SHA-256.