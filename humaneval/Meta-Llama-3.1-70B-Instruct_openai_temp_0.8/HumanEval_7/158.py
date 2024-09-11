```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): A substring to search for in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
```

This script uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring. The `in` operator is used to check if the substring is present in each string. The test cases from the problem statement are included at the end to verify the correctness of the function.