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
    return [s for s in strings if substring in s]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script uses a list comprehension to filter the input list of strings. It checks each string in the list to see if it contains the given substring, and if so, includes it in the output list.

You can run this script directly in a Python environment to test the `filter_by_substring` function. The example usage at the end demonstrates how to call this function with different inputs and prints the results.