```python
from typing import List
def concatenate(strings: List[str]):
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
    assert concatenate([None]) == 'None'
    assert concatenate(['a', 'aa', 'b', 'bb']) == 'abbb'
```
The function concatenate in the code takes a list of strings as an argument and returns a string that concatenates all the strings in the list. The test_concatenate function contains some additional tests to verify the correctness of the concatenate function.