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
def test_concatenate() -> None:
    """ Test the concatenate function
    Args:
        None
    """
    assert concatenate([]) == '', 'Should return empty string for an empty list'
    assert concatenate(['a']) == 'a', 'Should return a single string for one string'
    assert concatenate(['a', 'b']) == 'ab', 'Should concatenate two strings'
    assert concatenate(['a', 'bc']) == 'abc', 'Should concatenate three strings'
def main() -> None:
    """ Main function to execute the test
    """
    test_concatenate()

if __name__ == "__main__":
    main()
```