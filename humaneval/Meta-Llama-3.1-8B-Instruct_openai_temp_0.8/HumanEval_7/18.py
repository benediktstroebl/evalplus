```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): Substring to filter by

    Returns:
    List[str]: Filtered list of strings
    """
    # Use a list comprehension to filter the input list
    # The 'if substring in string' condition checks if the substring is in each string
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on the presence of the given substring. The test cases at the end demonstrate the function's behavior.