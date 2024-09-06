```python
from typing import List
def concatenate(strings: List[str]) -> str:
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
    assert concatenate([21]) == '21'
```
The provided Python script defines a function **concatenate** that takes a list of strings as an argument and concatenates them into a single string. The test_concatenate function then passes several tests to the **concatenate** function, which verifies the correctness of the concatenation operation.