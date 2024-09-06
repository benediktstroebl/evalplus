Here is a self-contained Python script that solves the problem of concatenating lists of strings into a single string:
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
```
This script provides a function `concat` that takes a list of strings as input and concatenates them into a single string, passing the test case as you provided.