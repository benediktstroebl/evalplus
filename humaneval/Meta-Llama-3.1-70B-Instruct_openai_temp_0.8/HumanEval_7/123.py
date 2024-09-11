```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter
    substring (str): A substring to filter by

    Returns:
    List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script uses a list comprehension to iterate over each string in the input list and checks if the substring is present in the string using the `in` operator. If the substring is found, the string is included in the output list.