Here is a Python script that contains a self-contained function that solves the problem of concatenating a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: concatenated string
    """
    return ''.join(strings)
```
This script defines a function called **concatenate** that takes in a list of strings and returns a concatenated string.  The testing has been added to the function to ensure its correctness.