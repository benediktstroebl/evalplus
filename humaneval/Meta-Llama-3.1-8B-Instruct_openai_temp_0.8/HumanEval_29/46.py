```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
    strings (List[str]): The list of strings to filter.
    prefix (str): The prefix to filter by.
    
    Returns:
    List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter strings that start with the given prefix
    return [string for string in strings if string.startswith(prefix)]

# Example use cases
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```

When you run this script, it will output:

```
[]
['abc', 'array']
```