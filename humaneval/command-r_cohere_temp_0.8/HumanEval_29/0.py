```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ 
    Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A new list containing only the strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]
```