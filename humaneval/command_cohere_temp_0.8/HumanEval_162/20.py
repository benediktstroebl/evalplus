```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts a string into MD5 and returns the result or None if the input is empty.
    """
    if text and text.strip():
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None

# Test Cases
def test_string_to_md5():
    md5_hash = '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('Hello world') == md5_hash
    assert string_to_md5('') is None
    assert string_to_md5('   ') is None

test_string_to_md5()
```

The function `string_to_md5` takes a string text as an argument and returns the MD5 hash of the string or None if the input is empty. The MD5 hash is a unique identifier for the string, usually generated as a 32-character hexadecimal code. The test cases ensure the function behaves as expected on 'Hello World' and empty strings. 

To execute the tests, the code relies on the `pytest` framework, which needs to be installed as follows:
```bash
pip install pytest
```

To run the tests, use the command `pytest`, and the tool will run all the test cases defined in the file. If all tests pass without any error, you will see a result like this:
```bash
....

======================================================================
ALL TESTS PASSED efficaciously in 0.001s
```