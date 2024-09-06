```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of string
    Returns:  string
    """
    return "".join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It also has several test cases to verify the correctness of the function:
- The `test_concatenate` function contains multiple assertions that check the output of the `concatenate` function for different inputs.