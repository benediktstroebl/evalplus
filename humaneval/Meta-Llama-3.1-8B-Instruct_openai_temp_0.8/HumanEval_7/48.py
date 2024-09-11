### Filter Strings by Substring
#### A Python Script to Filter a List of Strings Containing a Given Substring

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: A new list containing only the strings that have the substring.

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
    print(f"Strings containing '{substring}': {result}")
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to create a new list containing only the strings that have the given substring. The result is then printed out in the example usage section.