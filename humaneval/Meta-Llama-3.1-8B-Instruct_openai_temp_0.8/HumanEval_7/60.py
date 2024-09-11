```markdown
### Filter Strings by Substring
#### Description
This script defines a function `filter_by_substring` to filter a list of strings based on a given substring.

#### Code

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: The list of strings that contain the given substring.

    Examples:
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
print(f"Strings containing '{substring}': {filtered_strings}")
```

#### Explanation
This script uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring. It does this by iterating over each string in the input list and checking if the substring is present in the string using the `in` operator. If the substring is found, the string is included in the new list. The function then returns this new list.