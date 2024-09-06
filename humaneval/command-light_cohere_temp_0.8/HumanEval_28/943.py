Here is a Python script with a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings
    Returns:
    str: Concatented string
    """
    return ''.join(strings)
```
The function concatenate takes a list of strings as input and returns a string. The function then joins the strings using the ''.join(strings) statement, which uses the join function from the string module to concatenate the strings in the list.