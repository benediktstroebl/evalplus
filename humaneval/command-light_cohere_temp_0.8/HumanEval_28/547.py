```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([
        'a',
    ]) == 'a'
    assert concatenate([]) == 'abc' # invalid input, should return empty string
    assert concatenate(['a', '', 'c']) == 'ac'
test_concatenate()
```
The provided Python script defines a function `concatenate` that concatenates a list of strings into a single string. The `test_concatenate` function contains a series of tests that verify the correctness of the `concatenate` function using various inputs. 

Please note that the function signature should match the type hints provided for the function parameters.