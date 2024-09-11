### Filter Strings by Prefix
#### Problem Statement
Filter an input list of strings only for ones that start with a given prefix.

#### Code
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings
        prefix (str): Prefix to filter by

    Returns:
        List[str]: Filtered list of strings

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(filtered_strings)  # Output: ['abc', 'array']
```

#### Explanation
The `filter_by_prefix` function uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a given prefix.

This solution is concise and readable, making it easy to understand and use. The provided example usage shows how to call the function and print the filtered list of strings.