```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to filter by

    Returns:
        List[str]: Filtered list of strings
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` which uses list comprehension to filter the input list of strings. The function returns a new list containing only the strings that include the given substring.

The test cases at the end of the script demonstrate the function's behavior with different inputs.