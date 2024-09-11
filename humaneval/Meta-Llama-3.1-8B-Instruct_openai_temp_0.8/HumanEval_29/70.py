```markdown
### Filter by Prefix Function

This Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix.

#### Code

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

#### Explanation

This function uses a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The `startswith` method is used to check if a string starts with the prefix.

The function is then tested with some example inputs to demonstrate its usage.
```