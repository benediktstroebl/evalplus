```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join("".join(strings)  )
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The function `concatenate` takes a list of strings as input and returns the concatenated string. It uses the words inside function which is the main goal of concatenating strings and this function achieves it. The test_concatenate function provides several test cases to ensure the correctness of the `concatenate` function.