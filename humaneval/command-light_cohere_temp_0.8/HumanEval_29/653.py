```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the list starts with the provided prefix. The function returns a list containing only the strings that match the condition.