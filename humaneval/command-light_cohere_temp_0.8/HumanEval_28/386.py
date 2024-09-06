```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return "".join(strings)

def test_concatenate():
    assert concatenate([]) == "", "Empty list should return the empty string"
    assert concatenate(['a']) == "a", "Should concatenate single element"
    assert concatenate(['a', 'b']) == "ab"
    assert concatenate(['a', 'bc']) == "abc"
    assert concatenate(['ab', 'cd']) == "abcd"
```

The code defines the function **concatenate** which takes a list of strings and returns their concatenation as a single string. The test_concatenate function verifies the expected behavior of the **concatenate** function for different inputs.