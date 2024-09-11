```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to search for in the list of strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script uses a list comprehension to filter the input list of strings. It iterates over each string in the list and checks if the substring is present in the string. If the substring is found, the string is included in the output list. The test cases provided with the problem are also included in the script to verify its correctness.