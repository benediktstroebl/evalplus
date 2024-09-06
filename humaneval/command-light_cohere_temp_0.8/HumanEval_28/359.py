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
    """ Function to test the concatenate function
    """
    assert concatenate([]) == "", "Should return empty string"
    assert concatenate(["a"]) == "a", "Should return a single string"
    assert concatenate(["a", "b"]) == "ab"
    assert concatenate(["a", "bc", "123"]) == "abc123"
```
This script defines a function **concatenate** that takes a list of strings as an argument and returns the concatenated string. It also has a testing function **test_concatenate** that checks the correctness of the **concatenate** function by passing different inputs and verifying the expected outputs.