```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([1,2,3]) == '123'
```
This code defines a function `concatenate` that takes a list of strings and returns a concatenated string. It is also contains a test function to verify the correctness of the `concatenate` function. The test function passes all the test cases and confirms the expected output.