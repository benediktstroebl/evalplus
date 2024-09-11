### Filtering a List of Strings by a Substring
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of input strings
        substring (str): Substring to search for

    Returns:
        List[str]: List of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]
```

### Example Usage
```python
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```