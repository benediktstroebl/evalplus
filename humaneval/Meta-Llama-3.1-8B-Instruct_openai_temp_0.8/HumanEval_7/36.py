```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to search for.

    Returns:
        List[str]: A new list containing only the strings that contain the given substring.

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['hello', 'world', 'python'], 'o'))
print(filter_by_substring(['apple', 'banana', 'cherry'], 'r'))
```

This script defines the `filter_by_substring` function, which uses list comprehension to filter the input list of strings based on the presence of the given substring. The test cases at the end of the script demonstrate the function's behavior with different inputs.