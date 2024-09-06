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
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([123]) == '123'
```
The code defines a function **concatenate** that takes a list of strings as an argument and concatenates them into a single string. It also provides a region of code called **test_concatenate** which is designed to check the correctness of the **concatenate** function by passing different test cases.