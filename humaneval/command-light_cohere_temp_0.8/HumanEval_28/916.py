Here is a self-contained Python script that solves the problem of joining strings in a list into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings to concatenate
    
    Returns:
    string: Concatenated string
    """
    return "".join(strings)
def test_concatenate() -> None:
    # Test the function
    strings = ["a", "b", "c"]
    expected = "abc"
    actual = concatenate(strings)
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print("Passed test!")
```
This script provides a function `concatenate` that takes a list of strings as input and returns the concatenated string. The `test_concatenate` function provides a simple test case to verify if the `concatenate` function works correctly by passing in a list of strings and comparing the expected and actual concatenated strings.