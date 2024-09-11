```markdown
### Filter Strings by Substring
#### A Python function to filter a list of strings based on a given substring

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to filter by

    Returns:
        List[str]: The filtered list of strings

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'

filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension for efficient string filtering. The example usage demonstrates how to use the function with a list of strings and a substring.