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
    # Use list comprehension to filter the input list
    # The 'if substring in string' condition checks if the substring is in each string
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses list comprehension to create a new list containing only the strings that contain the substring. The test cases at the end demonstrate the function's behavior.