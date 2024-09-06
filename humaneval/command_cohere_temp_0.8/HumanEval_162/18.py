```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if text.strip() == "":
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

# Test Cases
md5_hello_world = '3e25960a79dbc69b674cd4ec67a72c62'
empty_string = None

assert string_to_md5('Hello world!") == md5_hello_world
assert string_to_md5('') == empty_string
``` 

This script imports the `hashlib` module that facilitates the creation of hash functions, it defines the `string_to_md5` function that takes a text string as an argument and returns its MD5 hash as a string or None if the text is empty. It verifies that the function behaves correctly against two test cases, one for a non-empty string and another for an empty string. 

The code for the `hashlib.md5()` function is `md5.update(text.encode('utf-8'))` which takes the text string, encodes it as UTF-8, and updates the MD5 hash object with the data. Then, the `md5.hexdigest()` method returns the hexadecimal representation of the hash.