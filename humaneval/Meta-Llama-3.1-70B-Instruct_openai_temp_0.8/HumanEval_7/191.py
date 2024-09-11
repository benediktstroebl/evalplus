```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter the input list
    # The 'if' condition checks if the substring is present in each string
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

# Additional test cases for edge cases
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], ''))  # ['abc', 'bacd', 'cde', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b'))  # ['abc', 'bacd']
```