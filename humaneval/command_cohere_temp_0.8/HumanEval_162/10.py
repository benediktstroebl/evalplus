```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Parameters:
    text (str): The input string to encrypt

    Returns:
    str or None: MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text: 
        return hashlib.md5(text.encode()).hexdigest() 
    else: 
        return None

# Tests
def test_string_to_md5():
    """
    Tests the string_to_md5 function for correct behavior.
    """
    assert string_to_md5("Hello World!") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
    assert string_to_md5("Allo Evryone!") != "3e25960a79dbc69b674cd4ec67a72c62"

# Run tests
test_string_to_md5()
```

The `hashlib.md5()` is used to hash the text to its MD5 equivalent, and the `hexdigest()` method returns the hash as a string. The function tests if the input string is empty, and if so, returns `None`. Additional tests verify that the function behaves correctly despite variations in the input text. 

The script tests the `string_to_md5()` function with various inputs and verifies that it produces the correct MD5 hash for the input text "Hello World!" and that it correctly returns `None` when the input is an empty string. 

To run the tests in the script you need to run the last test function as follows:
```python
test_string_to_md5()
``` 

This will run the test cases and assert that the function performs according to expectation.  If all tests pass, the output will not contain any messages and the function will return immediately. In the event that a test fails, a detailed description of the failure will be provided in the output to help you identify the source of the problem.