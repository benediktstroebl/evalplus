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
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([123]) == "123"
```
The function `concatenate` takes a list of strings as input and concatenates them into a single string. The `test_concatenate` function contains several tests to ensure the correctness of the `concatenate` function.