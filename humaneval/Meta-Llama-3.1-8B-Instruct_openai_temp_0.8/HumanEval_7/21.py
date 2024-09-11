```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered.
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
filtered_strings = filter_by_substring(strings, substring)

print(f"Original strings: {strings}")
print(f"Substring to search for: {substring}")
print(f"Filtered strings: {filtered_strings}")
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings. It then demonstrates the function's usage with an example. The output of the script will be the original list of strings, the substring to search for, and the filtered list of strings.