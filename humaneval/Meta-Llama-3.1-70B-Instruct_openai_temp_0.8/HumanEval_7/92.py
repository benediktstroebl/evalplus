```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): List of strings to filter.
    substring (str): Substring to search for.

    Returns:
    List[str]: Filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

# Additional test cases for thoroughness
print(filter_by_substring(['apple', 'banana', 'avocado'], 'av'))  # ['avocado']
print(filter_by_substring(['red', 'blue', 'green'], 'yellow'))  # []
```