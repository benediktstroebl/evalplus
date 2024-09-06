```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(*strings)

def test_concatenate():
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['']) == ''
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['a', '']) == 'a'
    assert concatenate([None]) == 'None'
    assert concatenate(['a', ' ', 'b']) == 'ab'
```
This code defines a function **concatenate** that takes a list of strings as input and concatenates them into a single string. It also provides several test cases that verify the correctness of the **concatenate** function with different input scenarios.