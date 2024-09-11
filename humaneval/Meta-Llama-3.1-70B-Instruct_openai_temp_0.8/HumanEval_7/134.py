```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring to be searched in the list of strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script uses a list comprehension to filter the input list of strings. The `in` operator checks if the substring is present in each string. If it is, the string is included in the output list. The test cases are provided to demonstrate the usage and correctness of the `filter_by_substring` function.