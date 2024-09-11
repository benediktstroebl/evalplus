```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The list of strings to be filtered
    substring (str): The substring to search for in the strings

    Returns:
    List[str]: A list of strings that contain the given substring

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test the function
print(filter_by_substring([], 'a'))  # Should print []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python', 'programming'], 'o'))  # Should print ['hello', 'programming']
```