```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and returns the result as a string.
    Returns None if the input is an empty string.

    Args:
        text (str): The string to encrypt.

    Returns:
        str or None: The MD5 hash of the input string if it is not empty, otherwise None.
    """
    if text.strip() == "":
        return None
    return hashlib.md5(text.strip().encode()).hexdigest()
```

The provided Python function uses the `hashlib` module to calculate the MD5 hash of the input string. It first checks if the input string is empty using the `strip` method to remove any leading or trailing whitespaces and then verifies if it's empty again. If the input string is empty, the function returns `None`. Otherwise, it uses the `hashlib.md5` method to encrypt the string and returns the result as a hexadecimal string using the `hexdigest` method. 

To verify the functionality of the provided solution, you can use the test case provided in the specification:
```python
def test_string_to_md5():
    """
    Test the string_to_md5 function.
    """
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"
    assert string_to_md5("") is None
``` 

This would ensure that the function behaves as expected, correctly encrypting the provided string and returning `None` for an empty input.  This approach ensures data integrity and security in the event of accidental disclosure of the stored data.  Depending of the use case, you could use this method to verify user input, ensuring it doesn't affect the application's behavior.