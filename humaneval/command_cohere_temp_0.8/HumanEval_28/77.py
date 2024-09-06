```python
# Import the list module from the typing module
from typing import List

# The function to concatenate the strings in the list
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    # If the list is empty, return an empty string
    if not strings:
        return ''

    # Use join() to concatenate the strings in the list with a space separator
    return ' '.join(strings)
```