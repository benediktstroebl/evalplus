```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to filter by

    Returns:
        List[str]: List of strings containing the given substring
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This Python script uses a list comprehension to filter the input list of strings. The list comprehension iterates over each string in the input list and checks if the given substring is present in the string. If the substring is found, the string is included in the output list. The function returns the filtered list of strings.