Here is a self-contained Python script that defines a function **filter_by_prefix**, which filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by prefix.

    Args:
        strings: List of strings to filter.
        prefix: str: Prefix to match
    """
    return [s for s in strings if s.startswith(prefix)]
```

You can use this function to filter a list of strings based on a given prefix. 

For example, if you provide the input list **['abc', 'bcd', 'cde', 'array']** and the prefix **'a', the output will be **['abc', 'array']**.