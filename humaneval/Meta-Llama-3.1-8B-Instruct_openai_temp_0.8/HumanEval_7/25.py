```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): Input list of strings to be filtered.
    substring (str): The substring to be searched in the strings.

    Returns:
    List[str]: A list of strings that contain the given substring.

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
print(filter_by_substring(strings, 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring([], 'a'))  # Output: []
```
In this script, the `filter_by_substring` function uses a list comprehension to create a new list that includes only the strings from the input list `strings` that contain the specified `substring`. The function takes advantage of the built-in string method `in` to check if a string contains the substring. The example usage demonstrates how to call the function with sample input and print the results.