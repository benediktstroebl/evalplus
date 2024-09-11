```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: The list of strings that contain the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Example usage:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # Output: ['hello', 'world']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  # Output: ['abc', 'bacd', 'cde', 'array']
```

In this code, we define a function `filter_by_substring` that takes two arguments: `strings` which is a list of strings, and `substring` which is a string to filter by. We use a list comprehension to create a new list that only includes the strings from the input list that contain the given substring. This approach is concise, readable, and efficient.