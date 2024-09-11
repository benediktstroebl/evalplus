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
    # Check if the input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings.")

    # Check if all elements in the list are strings
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings.")

    # Use the join() method to concatenate all strings in the list
    return ''.join(strings)


# Test cases
if __name__ == "__main__":
    print(concatenate([]))  # Expected output: ''
    print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
    print(concatenate(['hello','', 'world']))  # Expected output: 'hello world'
    try:
        print(concatenate(['a', 2, 'c']))  # Expected error: ValueError
    except ValueError as e:
        print(e)
    try:
        print(concatenate('a'))  # Expected error: TypeError
    except TypeError as e:
        print(e)
```

This script defines a function `concatenate` that takes a list of strings and returns their concatenation as a single string. It also includes test cases to ensure the function works correctly for different inputs. If the input is not a list or contains non-string elements, it raises a `TypeError` or `ValueError` respectively.