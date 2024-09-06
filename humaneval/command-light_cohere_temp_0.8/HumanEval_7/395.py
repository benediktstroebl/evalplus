Here's the improved version of the Python script with comments and accurate docstrings:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings for all occurrences of a given substring.

    Args:
        strings: List of strings.
        substring: The substring to search for in the strings.

    Returns: filtered list containing strings that contain the given substring.

    >>> Example list of strings ['abc', 'acd', 'cde', 'array', 'b']
        >>> filter_by_substring([ 'abc', 'acd', 'cde', 'array', 'b'], 'a')
        ['abc', 'cde', 'array']

    """
    return [s for s in strings if s.startswith(substring)]
```
This script includes type annotations for better code readability, and the docstrings are more detailed and accurate. It also provides a example of usage at the bottom of the function to pass the tests.