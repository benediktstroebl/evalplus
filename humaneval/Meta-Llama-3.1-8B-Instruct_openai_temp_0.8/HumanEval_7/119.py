### Filter Strings by Substring

The following Python script defines a function `filter_by_substring` that filters a list of strings for those containing a given substring.

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to search for.

    Returns:
        List[str]: List of strings containing the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'

result = filter_by_substring(strings, substring)
print(f"Strings containing '{substring}': {result}")
```

This script uses a list comprehension to filter the input list of strings based on whether each string contains the given substring. The result is a new list containing only the strings that match the condition.