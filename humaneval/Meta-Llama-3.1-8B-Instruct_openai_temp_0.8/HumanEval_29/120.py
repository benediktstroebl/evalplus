### Filter By Prefix Function
```markdown
### filter_by_prefix.py
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Example usage
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array']
    prefix = 'a'
    filtered_strings = filter_by_prefix(strings, prefix)
    print(f"Strings starting with '{prefix}': {filtered_strings}")
```
This script defines the `filter_by_prefix` function, which uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method of the string is used to check for prefixes. The example usage demonstrates how to use the function.