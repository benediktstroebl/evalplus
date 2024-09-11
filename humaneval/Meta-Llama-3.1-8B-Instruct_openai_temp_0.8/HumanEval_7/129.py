```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to be searched in the input strings

    Returns:
        List[str]: The filtered list of strings that contain the given substring

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # Output: ['hello', 'world']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to create a new list that only includes strings from the input list that contain the given substring. The example usage section demonstrates how to use this function with several different inputs.