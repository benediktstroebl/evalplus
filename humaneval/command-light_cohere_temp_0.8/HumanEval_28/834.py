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

# Test cases
strings = ["a", "b", "c"]
test_concat = concatenate(strings)
print("Test case 1:", test_concat)
strings = []
test_concat = concatenate(strings)
print("Test case 2:", test_concat)
strings = ["a", " ".join(i) for i in range(3)]
test_concat = concatenate(strings)
print("Test case 3:", test_concat)
```