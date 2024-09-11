```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): Input list of strings to be filtered.
    substring (str): Substring to filter the input list by.

    Returns:
    List[str]: Filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```