```python
# Importing required module
from typing import List


# Defining function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty lists return an empty string.
    """
    result = ''.join(strings)
    return result
```

The `concatenate` function uses the `join` method to combine all the strings in the list into a single string, and returns the result. Since the result of `join` for an empty list is an empty string, the function handles the edge case of an empty list gracefully, without needing an additional special case in the code. The empty list test case demonstrates this in the comment.