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
    """Function to test the concatenate function"""
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([None, 'a']) == 'a'
    assert concatenate(['a', '123']) == '123a'
if __name__ == "__main__":
    test_concatenate()
```