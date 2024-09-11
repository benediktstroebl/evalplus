```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to search for in each string

    Returns:
        List[str]: A list of strings that contain the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    strings_to_filter = ['abc', 'bacd', 'cde', 'array']
    substring_to_search = 'a'
    filtered_strings = filter_by_substring(strings_to_filter, substring_to_search)
    print(f"Strings containing '{substring_to_search}': {filtered_strings}")
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this in a concise and efficient way.

The script also includes an example usage in the `if __name__ == "__main__":` block, which demonstrates how to call the `filter_by_substring` function and print the result.