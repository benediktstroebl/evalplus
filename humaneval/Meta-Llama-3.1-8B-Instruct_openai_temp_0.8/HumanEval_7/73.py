```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring.lower() in s.lower()]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello', 'Hello']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(f"Filtered strings containing '{substring}': {filtered_strings}")
```

In this script, the function `filter_by_substring` uses a list comprehension to generate a new list containing only the strings from the input list that contain the specified substring. It uses the `lower()` method to make the comparison case-insensitive.

The example usage at the end of the script demonstrates how to call the function with a sample list of strings and a substring, and prints the result.