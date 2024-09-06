```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if text:
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None

# Unit tests:
def test_handles_empty_string():
    """
    Test the function's behavior when an empty string is passed in.

    Expectations:
        The function should return None.
    """
    assert string_to_md5("") is None

def test_encrypts_to_md5():
    """
    Test the function's ability to encrypt a string to its MD5 hash.

    Expectations:
        The return value should be the MD5 hash of the input string.
    """
    assert string_to_md5("Hello World") == "3e25960a79dbc69b674cd4ec67a72c62"
```
The MD5 hash algorithm is encapsulated within the function using the `hashlib` module. It calculates the hash of the input text and returns it as a string. If the input is not provided (i.e., `text` is `None`), the function returns `None`. 

The unit tests ensure that the function handles an empty string gracefully and correctly encrypts a string to its MD5 hash.