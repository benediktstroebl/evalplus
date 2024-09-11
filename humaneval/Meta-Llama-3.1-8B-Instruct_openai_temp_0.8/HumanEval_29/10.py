```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the strings
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```

In this script, we use a list comprehension to create a new list that only includes the strings from the input list that start with the given prefix. The `startswith()` method is used to check if a string starts with the prefix. This method returns `True` if the string starts with the prefix and `False` otherwise.