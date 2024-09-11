### Filtering Strings by Prefix

Here's a Python script that defines a function `filter_by_prefix` to filter a list of strings based on a given prefix:

```markdown
### Code

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
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
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Filtered strings with prefix '{prefix}': {filtered_strings}")
```

### Explanation

This script defines a function `filter_by_prefix` that takes two arguments: `strings` (a list of strings) and `prefix` (a string to filter by). It uses a list comprehension to create a new list that only includes strings from the input list that start with the given prefix.

The `startswith` method is used to check if each string starts with the given prefix. If a string matches, it is included in the new list.

Finally, the script demonstrates how to use the `filter_by_prefix` function with an example list of strings and a prefix.