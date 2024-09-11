```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, then returns a new list containing only the strings that include the given substring. It uses a list comprehension to achieve this in a concise and readable way.

To use this function, you can call it with a list of strings and a substring as arguments. The function will return a new list containing the filtered strings. The example usage at the end of the script demonstrates this with two test cases.