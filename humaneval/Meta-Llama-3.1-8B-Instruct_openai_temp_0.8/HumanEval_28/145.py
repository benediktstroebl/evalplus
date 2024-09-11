```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method takes an iterable of strings and concatenates them
    # The empty string '' is used as the separator
    return ''.join(strings)


# Test cases
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate()` that takes a list of strings as input and returns a single string by concatenating all strings in the list. The `join()` method is used to concatenate the strings. The test cases at the end demonstrate the function's behavior with different inputs.