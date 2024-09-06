```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: List of strings
    Returns:
        str: Concaten of strings
    """
    return "".join("".join(strings))
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The script defines a `concatenate` function that takes a list of strings as an argument and returns the concatenation of those strings as a single string. It also includes a test_concatenate function that contains asserts to test the correctness of the `concatenate` function.