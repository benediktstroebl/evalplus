```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    The filter is based on the insertion of the prefix into each string.
    Args:
        strings: List of strings.
        prefix: str
    Returns the filtering
    Returns: List of strings that start with the given prefix.
    """
    filtered_strings = strings
    filtered_strings = [s for s in strings if s.startswith(prefix)]
    return filtered_strings
```
This function allows you to filter a list of strings for those that start with a given prefix. It achieves this by iterating through a list comprehension, checking if each string starts with the specified prefix. The function returns a list containing the filtered strings.