```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
test_strings = ['abc', 'bacd', 'cde', 'array']
test_substring = 'a'
print(filter_by_substring(test_strings, test_substring))  # Output: ['abc', 'bacd', 'array']

empty_list = []
empty_substring = 'a'
print(filter_by_substring(empty_list, empty_substring))  # Output: []
```