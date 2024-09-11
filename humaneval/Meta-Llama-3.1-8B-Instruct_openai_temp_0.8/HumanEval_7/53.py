```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to search for in each string.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

In this script, we define a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. The list comprehension iterates over each string in the input list and checks if the substring is present in the string using the `in` operator. If the substring is found, the string is included in the output list. The function returns this list of filtered strings. The example usage at the end demonstrates how to use this function with a sample input list and substring.