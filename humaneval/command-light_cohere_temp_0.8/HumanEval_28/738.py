```python
from typing import List
def concatenate(strings: List[str]):
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
if __name__ == "__main__":
    test_concatenate()
```
This code defines the **concatenate** function, which takes a list of strings as input and concatenates them into a single string, then passes the test suite to verify the correctness of the function.

Please note that this code is fully self-contained and can be copied and pasted into any environment without the need for external imports or modules.