```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string that is the concatenation of all strings in the input list.
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method requires all strings to be concatenated to be in the same order
    # It takes an iterable (like a list) of strings as an argument
    return ''.join(strings)


# Test cases
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of all strings in the input list. The `join()` method is used to concatenate the strings. The script also includes test cases to verify that the function works correctly.