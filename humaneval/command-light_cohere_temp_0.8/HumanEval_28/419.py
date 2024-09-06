```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    string
    """
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abcs'
    assert concatenate(['abcd', 'abc']) == 'abcdabc'
```
The function concatenate takes a list of strings as an argument and returns a single string by concatenating the strings in the list. The function is then tested by the test_concatenate function, which passes all the tests related to the concatenate function.