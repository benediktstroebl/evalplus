```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to search for

    Returns:
        List[str]: The list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to iterate over the input list of strings. For each string, it checks if the substring is present using the `in` operator. If the substring is found, the string is included in the output list. The function returns the filtered list of strings. The example usage demonstrates how to call the function with a list of strings and a substring, and print the resulting filtered list.