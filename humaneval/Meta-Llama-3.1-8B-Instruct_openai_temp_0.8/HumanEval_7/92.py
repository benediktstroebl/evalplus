```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of input strings
        substring (str): The substring to look for in the input strings

    Returns:
        List[str]: The filtered list of strings
    """
    # Use list comprehension to filter the input list
    return [s for s in strings if substring in s]

# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses list comprehension to achieve this in a concise and efficient way. The test cases at the end demonstrate its usage.