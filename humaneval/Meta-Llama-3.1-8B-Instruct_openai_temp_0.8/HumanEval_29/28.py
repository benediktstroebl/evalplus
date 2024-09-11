### Filter by Prefix Function
#### Filter an input list of strings only for ones that start with a given prefix.

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix that the strings should start with.

    Returns:
    List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter the input list
    # The condition 'if string.startswith(prefix)' checks if the string starts with the prefix
    # If it does, the string is included in the new list
    return [string for string in strings if string.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function uses list comprehension to achieve this in a concise and efficient way. The test cases at the end demonstrate the function's behavior.