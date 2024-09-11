```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered
    substring (str): The substring that needs to be present in the strings

    Returns:
    List[str]: A list of strings that contain the given substring
    """
    # Use list comprehension to filter the strings
    # The 'if substring in string' condition checks if the substring is present in the string
    filtered_strings = [string for string in strings if substring in string]
    
    return filtered_strings


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that have the given substring. It includes test cases to verify the function's correctness.