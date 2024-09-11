```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to filter by

    Returns:
        List[str]: Filtered list of strings containing the given substring
    """
    return [string for string in strings if substring.lower() in string.lower()]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'x'))  # []
print(filter_by_substring(['Abc', 'BACD', 'CDE', 'Array'], 'a'))  # ['Abc', 'BACD', 'Array']
```

In this script, we use a list comprehension to iterate over the input list of strings and filter out the ones that do not contain the given substring (case-insensitive). The filtered list is then returned. The test cases at the end of the script demonstrate the functionality of the `filter_by_substring` function.