```markdown
### Filter Strings by Substring
#### A Python function to filter a list of strings based on a given substring.

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The input list of strings to filter.
    substring (str): The substring to search for in each string.

    Returns:
    List[str]: A list of strings that contain the given substring.

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```
This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on the presence of the given substring. The example usage demonstrates how to use this function to filter a list of strings.