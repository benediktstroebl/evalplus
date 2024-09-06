```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([['a'], ['b'], ['c']) == 'aabc'
```
The code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test_concatenate function verifies the correctness of the `concatenate` function by passing various test cases.