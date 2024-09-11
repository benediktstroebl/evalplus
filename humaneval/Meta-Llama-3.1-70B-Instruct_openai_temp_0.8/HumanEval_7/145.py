```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The input list of strings
    substring (str): The substring to filter by

    Returns:
    List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

In this script, we use list comprehension to iterate over the input list of strings and only include strings that contain the given substring. The `in` operator is used to check if a string contains the substring.

You can save this script to a file (e.g., `filter_by_substring.py`) and run it using Python (e.g., `python filter_by_substring.py`). The example usage at the end of the script will print the results of the example use cases.