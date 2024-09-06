```python
# Importing the necessary module
from typing import List


# Defining the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # If the input list is empty, return an empty string
    if not strings:
        return ''
    
    # Otherwise, concatenate the strings using the '+'' operator and a space as a separator
    return ' '.join(strings)
```