```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings to be filtered.
        substring (str): Substring to filter by.

    Returns:
        List[str]: List of strings containing the given substring.
    """
    return [string for string in strings if substring in string]

# Example use cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This Python script uses list comprehension to filter the input list of strings. It checks if the substring is present in each string and includes it in the output list if it is. The function is well-documented and includes example use cases to demonstrate its usage.