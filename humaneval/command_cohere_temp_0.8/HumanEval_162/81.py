```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()
```

This Python script uses the `hashlib` module to generate an MD5 hash. The `string_to_md5` function accepts a text string and returns its MD5 hash as a string, or `None` if the input is an empty string. 

The function incorporates the `utf-8` encoding to handle text input, and the `hexdigest()` method to return the hash in hexadecimal format.

To confirm its effectiveness, let's test the function using the example cited in the problem statement:
```python
test_string = 'Hello world'
expected_result = '3e25960a79dbc69b674cd4ec67a72c62'

result = string_to_md5(test_string)

if result == expected_result:
    print('Test passed.')
else:
    print('Test failed.')
```

This will generate the following output:
```bash
Test passed.
``` 

This demonstrates the validity of the MD5 hash generation for the `test_string`. 

Also, as an alternative approach, you can use the `hash()` function introduced in Python 3.9:
```python
import hashlib

def string_to_md5(text: str) -> str or None:
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This approach uses the `hashlib.md5()` method to return a hash object, and the `hexdigest()` method to convert it to a hexadecimal string.