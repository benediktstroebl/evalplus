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
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([None, 'a']) == 'a'
    assert concatenate([1, 2, 3]) == '123'
```
This Python script defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. The function uses the  list comprehension to concatenate the strings and returns the result as a string. The **test_concatenate** function contains several tests that verify the correctness of the **concatenate** function.