```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to search for in each string

    Returns:
        List[str]: List of strings that contain the given substring
    """
    # Use list comprehension to create a new list that includes only strings
    # that contain the substring
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses list comprehension to efficiently create the new list. The test cases at the end demonstrate the function's behavior.