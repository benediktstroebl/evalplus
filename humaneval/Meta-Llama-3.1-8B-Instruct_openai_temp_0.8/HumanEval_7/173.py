```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of input strings
    substring (str): The substring to filter by

    Returns:
    List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses a list comprehension to create a new list that only includes strings that contain the given substring. The script also includes two test cases to demonstrate the function's behavior.