```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return "".join("".join(strings))
def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string.  The test_concatenate function contains assertions that check the correctness of the `concatenate` function by passing various input strings and verifying the expected output.