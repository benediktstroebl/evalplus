Here is the Python script that solves the problem:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings
    """
    return [string for string in strings if substring in string]

# Example use cases:
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['hi', 'hello', 'world'], 'l'))
```