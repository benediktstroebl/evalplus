```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code provides a function called **concatenate** that takes in a list of strings as an argument and returns the concatenated string. The test_concatenate function tests if the **concatenate** function is working correctly by passing different lists of strings and verifying if the output is correct.