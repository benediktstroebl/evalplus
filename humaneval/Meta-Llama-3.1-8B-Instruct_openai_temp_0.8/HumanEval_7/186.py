Here's a self-contained Python script that solves the given problem:

```markdown
### Filter Strings by Substring

#### Problem Description

Filter an input list of strings only for ones that contain a given substring.

#### Code

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to filter.
    substring (str): A substring to search for in the input strings.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example Usage:
strings_to_filter = ['abc', 'bacd', 'cde', 'array']
substring_to_search = 'a'
filtered_strings = filter_by_substring(strings_to_filter, substring_to_search)
print(filtered_strings)
```

#### Explanation

This code uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring. The `in` operator is used to check if the substring is present in each string. This approach is concise, readable, and efficient, making it suitable for filtering large lists of strings.