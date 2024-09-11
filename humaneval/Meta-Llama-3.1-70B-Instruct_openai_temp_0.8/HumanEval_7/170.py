```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to filter by.

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
    input_strings = ['abc', 'bacd', 'cde', 'array']
    substring_to_filter = 'a'
    result = filter_by_substring(input_strings, substring_to_filter)
    print(result)  # Output: ['abc', 'bacd', 'array']
```