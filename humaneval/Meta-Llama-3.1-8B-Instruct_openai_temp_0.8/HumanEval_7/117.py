```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for in each string

    Returns:
        List[str]: Filtered list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring. The `if substring in s` condition filters the strings based on the presence of the substring. The function is then tested with the provided example use cases.