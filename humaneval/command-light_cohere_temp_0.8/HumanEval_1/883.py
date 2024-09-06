```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separated parenthesis
    """
    return [x for x in s.split(' ')]
```
The function split() creates the list of strings by splitting the input string by spaces.