```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to filter by

    Returns:
        List[str]: A list of strings that contain the given substring

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'l'))  # ['hello', 'world']
print(filter_by_substring(['apple', 'banana', 'cherry'], 'n'))  # ['banana']
```

In this code, I've used a list comprehension to filter the input list of strings based on the presence of the given substring. This is a concise and efficient way to perform the filtering operation. The test cases at the end demonstrate the function's behavior for different inputs.