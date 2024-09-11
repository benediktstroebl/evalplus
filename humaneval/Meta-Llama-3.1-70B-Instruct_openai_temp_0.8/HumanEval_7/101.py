```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A new list containing only the strings that have the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
print("All tests passed.")
```

In this script, we define a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. It checks each string to see if the given substring is present, and if so, includes it in the new list. We also include some test cases to verify that the function works correctly.