```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return "".join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the documents the time to provide a self-contained function that solves the problem and passes the tests. The `test_concatenate` function checks the correctness of the `concatenate` function by passing the input tests.