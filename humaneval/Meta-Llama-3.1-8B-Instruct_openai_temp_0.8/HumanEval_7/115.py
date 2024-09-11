```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): Input list of strings
    substring (str): Substring to be searched

    Returns:
    List[str]: List of strings containing the given substring

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)
```

In this script, we define a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this. The example usage demonstrates how to call this function with a list of strings and a substring, and print the result.