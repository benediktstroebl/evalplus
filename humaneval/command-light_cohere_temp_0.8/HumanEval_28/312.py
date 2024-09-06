```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == '', 'Empty list should return the empty string'
    assert concatenate(['a']) == 'a', 'Single string should be returned'
    assert concatenate(['a', 'b', 'c']) == 'abc', 'List of three strings should be concatenated'
# Test cases
test_concatenate()
```
The function concatenate takes a list of strings and returns a string by concatenating the strings in the list. The test_concatenate function contains test cases that verify the correctness of the concatenate function.