```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: Filtered list of strings containing the substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # Output: ['hello', 'world']
    print(filter_by_substring(['abc', 'def'], 'xyz'))  # Output: []
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses a list comprehension to create a new list containing only the strings that have the substring. The function is then tested with several example use cases.