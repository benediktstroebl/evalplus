Here is a simple Python script that defines the `filter_by_substring` function and includes docstrings for documentation:

```markdown
### Filter by Substring
#### Problem Description

Filter an input list of strings only for ones that contain given substring.

#### Code
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings to filter.
        substring (str): The substring to search for in each string.

    Returns:
        List[str]: A new list containing only the strings that contain the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]
```

#### Usage Example
```python
# Test the function
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'

filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The function includes a docstring with documentation and example use cases. The script also includes a usage example at the end to demonstrate how to use the function.