```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter.
    substring (str): The substring to search for.

    Returns:
    List[str]: The filtered list of strings.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'world']
```