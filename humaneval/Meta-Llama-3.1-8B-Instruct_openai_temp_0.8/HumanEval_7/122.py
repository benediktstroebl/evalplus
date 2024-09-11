### Filter Strings by Substring
#### Python Script
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The test cases demonstrate the function's behavior with empty input and a non-empty input list.