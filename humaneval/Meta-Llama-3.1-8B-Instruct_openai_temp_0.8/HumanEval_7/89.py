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
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which filters a list of strings based on whether they contain a given substring. The function uses a list comprehension to create a new list that includes only the strings that contain the substring. The script also includes an example usage of the function at the end.