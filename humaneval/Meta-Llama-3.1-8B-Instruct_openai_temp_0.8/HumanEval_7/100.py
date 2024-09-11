```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    - strings (List[str]): A list of strings to filter
    - substring (str): A substring to search for

    Returns:
    - List[str]: A filtered list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]

# Example usage:
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this.

The example usage at the end demonstrates how to use this function. It filters an empty list and a list of strings containing the substring 'a', and prints the results.