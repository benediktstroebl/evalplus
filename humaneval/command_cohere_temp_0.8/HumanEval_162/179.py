```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Return the MD5 hash of the string text as a lowercase hexadecimal string.
    If the input is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest().lower()
```
The function uses the hashlib library in Python which implements a secure hash algorithm, MD5, with the update method to update the hash value with the text and the hexdigest method to retrieve the hexadecimal representation of the calculated hash value. The returned value is then lowered to ensure the correct capitalization of the hexadecimal digits. 

This script satisfies the test case provided in the prompt, as well as the aforementioned test case:
```python
def test_string_to_md5():
    """
    Test the string_to_md5 function.
    """
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('abc') != '3e25960a79dbc69b674cd4ec67a72c62'
```
Please note that MD5 is no longer considered secure due to vulnerabilities, and it is recommended to use a more secure hash function for security-sensitive applications.