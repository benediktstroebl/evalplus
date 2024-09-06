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
    assert concatenate(['a', '', 'c']) == 'ac'
    assert concatenate([None]) == 'None'
```
The above Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It also contains a detailed test cases that cover various scenarios, such as empty lists, single strings, multiple strings, empty strings, and strings with none.