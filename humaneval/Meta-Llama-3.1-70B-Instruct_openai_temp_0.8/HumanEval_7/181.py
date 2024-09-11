```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    - strings (List[str]): The input list of strings.
    - substring (str): The substring to filter by.

    Returns:
    - List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, a list comprehension is used to create a new list that includes only the strings that contain the given substring. The `in` operator checks if the substring is present in each string. This approach is efficient and readable, making it suitable for filtering lists of strings based on a substring.