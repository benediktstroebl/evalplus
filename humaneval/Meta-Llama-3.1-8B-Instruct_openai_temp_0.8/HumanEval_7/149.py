```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to filter by

    Returns:
        List[str]: Filtered list of strings containing the substring
    """
    # Use list comprehension to filter the input list
    # The 'if' condition checks if substring is present in each string
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    # Empty list test case
    print(filter_by_substring([], 'a'))  # Expected output: []

    # Non-empty list test case
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. The function uses a list comprehension to achieve this in a concise way. The test cases are also included to demonstrate the function's behavior.