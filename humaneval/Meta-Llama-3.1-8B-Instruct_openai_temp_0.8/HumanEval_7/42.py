### Filter Strings by Substring
#### Python Script
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to filter by

    Returns:
        List[str]: Filtered list of strings

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'xyz']
substring = 'a'

filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to filter the input list and return only the strings that contain the given substring. The function includes docstrings for documentation and example usage.