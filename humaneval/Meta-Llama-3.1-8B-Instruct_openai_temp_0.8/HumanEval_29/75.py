### Filter Strings by Prefix
#### Python Script
```markdown
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): The input list of strings.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: The filtered list of strings.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage
strings = ['abc', 'bcd', 'cde', 'array', 'xyz']
prefix = 'a'

filtered_strings = filter_by_prefix(strings, prefix)
print(f"Filtered strings with prefix '{prefix}': {filtered_strings}")
```

### Explanation
The `filter_by_prefix` function uses list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a given prefix. If the prefix is an empty string, this method will return True for any string, as an empty string is considered to be a prefix of every string. 

The function takes two parameters: `strings`, the input list of strings, and `prefix`, the prefix to filter by. It returns the filtered list of strings.

In the example usage, we define a list of strings and a prefix, then call the `filter_by_prefix` function with these parameters. The filtered list of strings is then printed to the console.