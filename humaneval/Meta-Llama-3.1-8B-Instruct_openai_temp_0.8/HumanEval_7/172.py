```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings
    """
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world'], 'l'))  # ['hello', 'world']
    print(filter_by_substring(['hello', 'world'], 'z'))  # []
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to filter out the strings that do not contain the given substring. The test cases at the end of the script verify that the function works correctly.