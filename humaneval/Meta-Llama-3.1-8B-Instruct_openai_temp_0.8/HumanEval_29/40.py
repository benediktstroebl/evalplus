```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['hello', 'world', 'python'], 'py'))  # Output: ['python']
```

This script uses list comprehension to create a new list containing only the strings that start with the given prefix. The `startswith()` method is used to check if a string starts with the prefix. The example usage demonstrates how to call the function with different inputs and print the results.