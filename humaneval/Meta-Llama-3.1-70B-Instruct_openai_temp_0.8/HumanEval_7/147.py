```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring that the strings should contain

    Returns:
        List[str]: A new list containing only the strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
print("All test cases pass")
```

This script defines a function `filter_by_substring` that uses list comprehension to create a new list containing only the strings that contain the given substring. It then runs two test cases to verify the correctness of the function.