### Filter by Prefix Function

The following Python script defines a function to filter a list of strings based on a given prefix. This function leverages list comprehension to efficiently create a new list with only the strings that start with the specified prefix.

```markdown
### Code

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array', 'banana']
    prefix = 'a'

    filtered_strings = filter_by_prefix(strings, prefix)

    print(f"Prefixed strings starting with '{prefix}':")
    print(filtered_strings)
```

### Explanation

This script consists of the following key elements:

*   A function, `filter_by_prefix`, takes two inputs: `strings`, a list of strings to filter, and `prefix`, the prefix to filter by.
*   The function leverages list comprehension to create a new list that includes only the strings from the input list that start with the specified prefix.
*   The `startswith` method is used to check if each string begins with the given prefix.
*   An example usage is demonstrated in the `if __name__ == "__main__"` block, which showcases how to call the `filter_by_prefix` function and print the filtered list of strings.