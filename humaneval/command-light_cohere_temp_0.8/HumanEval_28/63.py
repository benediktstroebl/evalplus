```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    """Test the concatenate function
    """
    assert concatenate([]) == '', 'Empty list should return empty string'
    assert concatenate(['a']) == 'a', 'Only one element should return'
    assert concatenate(['a', 'b', 'c']) == 'abc', 'List should be concatenated'
    assert concatenate(['a', 'b']) == 'ab', 'Overwriting should still work'
if __name__ == "__main__":
    test_concatenate()
```