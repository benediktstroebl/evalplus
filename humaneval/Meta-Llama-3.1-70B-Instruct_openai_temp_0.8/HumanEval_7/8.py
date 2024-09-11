```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to look for

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. The function returns a new list containing only the strings that contain the given substring.

The test cases at the end of the script demonstrate the function's correctness. They verify that the function behaves as expected for an empty input list and for a non-empty input list with some strings containing the substring and others not containing it.