```markdown
### Filter Strings by Substring
#### A Python Script to Filter an Input List of Strings Only for Ones that Contain a Given Substring

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to search for in the strings

    Returns:
        List[str]: Filtered list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_strings = filter_by_substring(strings, substring)
    print(f"Strings containing '{substring}': {filtered_strings}")
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. It uses a list comprehension to achieve this.

The `if __name__ == "__main__":` block provides an example usage of the function, which prints the filtered list of strings to the console.