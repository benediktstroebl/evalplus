```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings
    :return: Concatenated string
    """
    return "".join(strings)
def test_concatenate() -> None:
    """ Function to test the concatenate function
    :return: None
    """
    assert concatenate([]) == "", "Empty list should return an empty string"
    assert concatenate(["a"]) == "a", "Single element list should return its element"
    assert concatenate(["a", "b"]) == "ab", "Two elements list should return concatenated string"
    assert concatenate(["a", "b", "c"]) == "abc", "Three elements list should return concatenated string"
test_concatenate()
```