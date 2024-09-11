```markdown
### Filter Strings by Prefix
#### Python Script

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): Input list of strings.
    prefix (str): Prefix to filter by.

    Returns:
    List[str]: List of strings that start with the given prefix.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```
This script uses a list comprehension to filter the input list of strings based on whether they start with the given prefix. It returns a new list containing only the strings that start with the prefix. The `startswith` method is used to check if a string starts with the prefix.