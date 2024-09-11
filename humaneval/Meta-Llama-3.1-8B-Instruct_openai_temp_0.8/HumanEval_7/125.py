```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings to be filtered
    substring (str): Substring to be searched in input strings

    Returns:
    List[str]: List of strings that contain the given substring

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    result = filter_by_substring(strings, substring)
    print(result)  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this. The example usage at the end demonstrates how to use this function with a list of strings and a substring.