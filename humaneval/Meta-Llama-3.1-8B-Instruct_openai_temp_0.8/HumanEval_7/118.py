```markdown
### Filter Strings by Substring
#### A Python function to filter a list of strings containing a given substring

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The list of strings to be filtered
    substring (str): The substring to look for in each string

    Returns:
    List[str]: The filtered list of strings

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

In this script, we define the `filter_by_substring` function that uses a list comprehension to filter the input list of strings based on the presence of the given substring. The function is then tested with some example inputs to demonstrate its correctness.