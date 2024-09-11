```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring to filter by.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, we define the `filter_by_substring` function using list comprehension, which creates a new list containing only the strings that include the specified substring. The function is then tested with the provided example inputs.