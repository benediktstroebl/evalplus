```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): The substring that must be present in the filtered strings

    Returns:
        List[str]: A list of strings containing the given substring
    """
    return [string for string in strings if substring in string]


# Example usage
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that have the given substring. The function uses list comprehension to create the new list, and the `in` operator to check if a string contains the substring.

You can run the script to test the function with the provided example use cases.