```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings for ones that start with a given prefix.
    : Return only the general strings starting with the specified prefix
    """
    return [string for string in strings if string.startswith(prefix)]
``` 
This function uses a list comprehension to filter out the strings that do not start with the specified prefix.