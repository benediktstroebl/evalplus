```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): A substring to search for in the input strings.

    Returns:
        List[str]: A list of strings containing the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
if __name__ == "__main__":
    input_list = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_list = filter_by_substring(input_list, substring)
    print(f"Strings containing '{substring}': {filtered_list}")
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings based on whether each string contains the given substring. The function returns a new list containing only the strings that match the search criteria. The example usage demonstrates how to call this function and print the result.