### Filter Strings by Substring
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: The list of strings containing the substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```
This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The function takes two inputs: `strings`, the list of strings to filter, and `substring`, the substring to search for. It returns the filtered list of strings. The example usage at the end demonstrates how to use the function.