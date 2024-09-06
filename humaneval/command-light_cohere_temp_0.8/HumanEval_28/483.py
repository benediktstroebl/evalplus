Here is a Python script that contains a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
        string
    """
    return "".join(strings)

strings = ["a", "b", "c"]
print(concatenate(strings)) # Output: "abc"
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns a string by concatenating the strings in the list. The output of the concatenate function is indeed "abc".