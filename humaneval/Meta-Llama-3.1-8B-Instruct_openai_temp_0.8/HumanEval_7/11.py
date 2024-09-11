```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    
    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to search for.
    
    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to create a new list that contains only the strings from the input list that contain the given substring. The function then returns this new list. The example usage at the end demonstrates how to use the function.