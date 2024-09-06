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

# Unit tests
def test_concatenate():
    strings = ['a', 'b', 'c']
    result = concatenate(strings)
    assert result == 'abc'

if __name__ == "__main__":
    test_concatenate()
```