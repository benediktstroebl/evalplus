```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to filter by

    Returns:
        List[str]: Filtered list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world'], 'x'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'c'))  # ['abc', 'bacd', 'cde']
```

This script uses a list comprehension to filter the input list of strings based on whether they contain the given substring. It also includes test cases to demonstrate its usage.