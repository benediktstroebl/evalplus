```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring that the strings should contain.
    
    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to filter the list of strings
    # The 'if' condition checks if the substring is present in each string
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that include the given substring. The function uses a list comprehension to achieve this in a concise and readable manner. The test cases at the end of the script demonstrate the function's behavior with different inputs.