```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([ '', 'a' ])
    'a'
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([ '', 'a' ]) == 'a'
    assert concatenate(['abc', '123']) == '123abc'
if __name__ == "__main__":
    test_concatenate()
``` 
This code defines a `concatenate` function that takes a list of strings and returns the concatenated string. It also has a test function that passes all the corresponding tests. The test function uses the test assertions to ensure the correctness of the `concatenate` function.