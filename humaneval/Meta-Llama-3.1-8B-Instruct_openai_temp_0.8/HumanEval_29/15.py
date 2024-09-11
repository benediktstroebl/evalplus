```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings that start with the given prefix.
    """
    # Use a list comprehension to filter the list of strings
    # The 'if' condition checks if each string starts with the given prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    return filtered_strings

# Test cases
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```

In this script:

1. We define a function `filter_by_prefix` that takes a list of strings `strings` and a prefix `prefix` as input.
2. We use a list comprehension to filter the list of strings. The `if` condition checks if each string starts with the given prefix using the `startswith` method.
3. We return the filtered list of strings.
4. We include two test cases to verify the function's behavior.