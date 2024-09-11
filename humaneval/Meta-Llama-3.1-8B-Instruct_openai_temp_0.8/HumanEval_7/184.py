```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of input strings.
    substring (str): The substring to search for.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Should print []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'h'))  # Should print ['hello']
```

This script defines a function `filter_by_substring` that filters a list of strings based on whether they contain a given substring. It uses a list comprehension to create a new list containing only the strings that contain the substring. The function is then tested with the provided example test cases.