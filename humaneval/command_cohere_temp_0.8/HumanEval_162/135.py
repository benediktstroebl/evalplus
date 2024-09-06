```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

# Tests
md5_hello_world = '3e25960a79dbc69b674cd4ec67a72c62'
test_string = 'Hello world'

if string_to_md5(test_string) == md5_hello_world:
    print('pass')
else:
    print('fail')

empty_test_string = ''

if string_to_md5(empty_test_string) is None:
    print('pass')
else:
    print('fail')
```

The above Python code defines a function `string_to_md5`, which accepts a string text and returns its MD5 hash as a string or None if the input is empty. It utilizes the hashlib module in Python to compute the MD5 hash. The tests section includes tests to validate the function's behavior against predefined values for Hello, World and an empty string. 

The output of the script will be: 
```python
pass
pass
```

The first test validates the correct behavior of the `string_to_md5` function for a non-empty string, and the second test validates the correct behavior of the function for an empty string.