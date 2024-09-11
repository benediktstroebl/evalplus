### Filter by Substring
#### Python Script

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to filter.
    substring (str): The substring to search for.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring([], 'a'))  # Output: []
```

### How it Works
This script uses a list comprehension to iterate over the input list of strings and returns a new list with only the strings that contain the given substring. The `in` operator is used to check if the substring is present in each string. If it is, the string is included in the output list.