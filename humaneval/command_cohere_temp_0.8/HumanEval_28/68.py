```python
# Importing required module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty list results in an empty string.
    """
    result = ''.join(strings)
    return result
```

The provided function uses the `join` method to combine all the strings in the list into a single string, and returns it. The `typing` module is used to create accurate type hints, indicating that the function takes a list of strings and returns a string.