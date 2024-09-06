```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    """ Test the concatenate function with various inputs """
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['a', ' ', 'b']) == 'ab'
    assert concatenate(['a', '\nb']) == 'ab'
    assert concatenate(['\nt', 'a']) == '\na'
    assert concatenate(['\t\ta']) == '\t\ta'
```
The function **concatenate** in the above code takes a list of strings as input and concatenates them into a single string. The test_concatenate function contains various tests to validate the correctness of the **concatenate** function.