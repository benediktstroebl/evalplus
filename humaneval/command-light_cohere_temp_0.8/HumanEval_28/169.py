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
The code provides a function concatenate that takes a list of strings as an argument and returns the concatenated string. The test case successfully passes the required inputs and returns the expected output for an empty list and a list with three strings.