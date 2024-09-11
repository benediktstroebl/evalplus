Here's the Python code that implements the `filter_by_prefix` function:
```markdown
# Filter a list of strings by a given prefix
------------------------------------------

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
    return [s for s in strings if s.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
The script uses a simple list comprehension to filter the input list of strings. The `startswith` method is used to check if each string starts with the given prefix.