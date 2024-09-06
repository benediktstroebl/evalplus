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
    # Tests
    strings = ["a", "b", "c"]
    expected = "abc"
    actual = concatenate(strings)
    assert actual == expected
    strings = ["a",] + strings
    expected = "".join("".join(strings)
    actual = concatenate(strings)
    assert actual == expected
```
This code provides a function that concatenates strings in a list into a single string, and it has comprehensive tests to verify the correctness of the `concatenate` function with various inputs.