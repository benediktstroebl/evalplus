```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings.
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


# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_strings = filter_by_substring(strings, substring)
    print(f"Strings containing '{substring}': {filtered_strings}")
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter a list of strings based on whether they contain a given substring. The function is then tested with example usage in the `if __name__ == "__main__":` block.