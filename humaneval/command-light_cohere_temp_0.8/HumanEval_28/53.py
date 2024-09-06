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
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'abcs'
    assert concatenate([]) == ''
```

The function concatenate in this code takes a list of strings as input and returns a single string by concatenating the strings in the list. The test_concatenate function contains several tests that validate the correctness of the concatenate function. 

You can use this code block as a starting point for solving the problem in Markdown code or any other format you prefer.