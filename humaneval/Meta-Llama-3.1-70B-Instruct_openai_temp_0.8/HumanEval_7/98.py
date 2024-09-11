```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to filter by

    Returns:
        List[str]: A new list containing only the strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, we use a list comprehension to create a new list containing only the strings that contain the given substring. The `in` operator is used to check if the substring is present in each string. The function returns this new list. The provided unit tests are also included in the script as example use cases.