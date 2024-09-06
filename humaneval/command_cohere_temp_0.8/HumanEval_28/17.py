```python
# The following code is adapted from https://www.geeksforgeeks.org/python-concatenate-elements-of-a-list-into-a-string/

from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    result = ''
    for string in strings:
        result += string
    return result

# Tests
def test_concatenate():
    """
    Tests for concatenate function
    """
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['Adolf', 'Hitler', 'was', 'a', 'bad', 'man']) == 'AdolfHitlerwasabadman'

test_concatenate()
```