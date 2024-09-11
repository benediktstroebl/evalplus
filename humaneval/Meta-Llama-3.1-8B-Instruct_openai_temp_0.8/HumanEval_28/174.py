```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: The concatenated string.
    """
    # Use the join method of the empty string to concatenate all strings in the list
    return ''.join(strings)

# Test cases
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines the `concatenate` function as specified. It uses the `join` method of the empty string (`''`) to concatenate all strings in the input list. The test cases at the end demonstrate the function's behavior for both an empty list and a non-empty list.