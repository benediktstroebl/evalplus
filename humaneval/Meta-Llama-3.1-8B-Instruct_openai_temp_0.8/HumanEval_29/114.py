### Filter Strings by Prefix
#### Python Script

```markdown
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings.
        prefix (str): Prefix to filter by.

    Returns:
        List[str]: Filtered list of strings.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Test the function
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['hello', 'world'], 'w'))  # Output: ['world']
```

This Python script defines a `filter_by_prefix` function that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to filter the input list.

The script also includes test cases in the `if __name__ == "__main__":` block to demonstrate how to use the `filter_by_prefix` function. You can run the script to see the output of these test cases.