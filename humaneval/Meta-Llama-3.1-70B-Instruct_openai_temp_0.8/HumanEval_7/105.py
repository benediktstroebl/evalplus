```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to filter.
    substring (str): A substring to filter by.

    Returns:
    List[str]: A list of strings containing the given substring.
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # Expected: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses list comprehension to filter an input list of strings. The function checks if each string in the input list contains the given substring using the `in` operator. The test cases provided in the docstring are also included in the script for demonstration purposes.