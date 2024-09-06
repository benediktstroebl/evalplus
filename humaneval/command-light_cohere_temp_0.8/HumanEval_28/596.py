```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: string"""
    strings = [str for str in strings]
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This code defines a function **concatenate** that takes a list of strings and concatenates them into a single string. It then defines a test_concatenate function with assert statements that test the functionality of the **concatenate** function with different inputs.