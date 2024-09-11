```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring that must be present in the string.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that uses list comprehension to filter the input list of strings. It checks each string to see if it contains the given substring, and if so, includes it in the output list. The function includes type hints for clarity and documentation. The example use cases at the end demonstrate the function's behavior with different inputs.