```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)

def test_concatenate() -> None:
    """ Function to test the concatenate function
    """
    assert concatenate([]) == '', "empty list"
    assert concatenate(['a']) == 'a', "single string"
    assert concatenate(['a', 'b', 'c']) == 'abc', "correct concatenation"
    assert concatenate(['a', 'bc']) == 'abc', "without extra separator"

if __name__ == "__main__":
    test_concatenate()
```
This Python script defines a function `concatenate` that takes a list of strings and returns their concatenated string. The `test_concatenate` function contains several tests to validate the correctness of the `concatenate` function.