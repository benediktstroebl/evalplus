```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

In this script, I've implemented the `filter_by_prefix` function using a list comprehension. This function takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix.

The example usage at the end demonstrates how to use the function. The function is called with two different inputs: an empty list and a list containing some strings that start with the prefix 'a'. The output of the function is printed to the console.

This script includes docstrings that provide a description of the function, its arguments, and its return value. This is good practice for making your code easy to understand and use.