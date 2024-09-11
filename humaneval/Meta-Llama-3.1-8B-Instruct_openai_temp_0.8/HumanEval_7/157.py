```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: Filtered list of strings containing the substring
    """
    # Use list comprehension to filter the input list
    # The 'if' condition in the list comprehension checks for the presence of the substring
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    # Test case 1: Empty list
    print(filter_by_substring([], 'a'))
    
    # Test case 2: List with substrings
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
    
    # Test case 3: No substrings found
    print(filter_by_substring(['cde', 'fgh'], 'a'))
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. It uses list comprehension to filter the input list efficiently. The test cases at the end demonstrate the function's behavior for different input scenarios.