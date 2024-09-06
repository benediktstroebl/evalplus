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
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
if __name__ == "__main__":
    test_concatenate()
```
This script provides a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The test function passes the banded tests, and the code is self-contained within the file, making it easy to include and test the function without needing external dependencies.