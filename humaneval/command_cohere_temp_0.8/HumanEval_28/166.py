```python
# Importing the required module
from typing import List


# Defining the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # If the input list is empty, return an empty string
    if not strings:
        return ''

    # Otherwise, concatenate the strings in the list and return the result
    return ''.join(strings)
```