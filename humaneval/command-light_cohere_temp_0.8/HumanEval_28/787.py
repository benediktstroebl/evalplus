```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :type strings: List[str]
    :rtype: str
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided Python script defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It also includes a test_concatenate function with several assertions to verify the correctness of the `concatenate` function.