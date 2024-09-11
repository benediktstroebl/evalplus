```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The input list of strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['apple', 'banana', 'orange', 'grape'], 'an'))  # ['banana', 'orange', 'grape']
```

This Python script uses list comprehension to create a new list containing only the strings that have the given substring. It does this by iterating over each string in the input list and checking if the substring is present in the string using the `in` operator. The result is a new list that contains only the strings that match the condition.