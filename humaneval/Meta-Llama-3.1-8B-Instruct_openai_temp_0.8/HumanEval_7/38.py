```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

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


# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    print(f"Filtering strings for substring '{substring}':")
    filtered_strings = filter_by_substring(strings, substring)
    print(filtered_strings)
```

This script defines the `filter_by_substring` function and demonstrates its usage in the `if __name__ == "__main__"` block. The function uses a list comprehension to filter the input list of strings, returning only the strings that contain the given substring.