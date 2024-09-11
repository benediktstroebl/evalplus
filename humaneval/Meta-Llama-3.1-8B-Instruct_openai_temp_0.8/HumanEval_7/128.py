Here's a Python function that filters a list of strings based on the presence of a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: Filtered list of strings containing the substring
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```
This function uses a list comprehension to create a new list containing only the strings from the input list that have the given substring. The `in` operator is used to check if each string contains the substring. If you need more complexity, let me know!