```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups and balanced (each open brace is properly closed and not nested within each other)
    Ignore any spaces in the input string.
    >>> '){}(()(){[{}'
    ['}', '(', '()', '[]']
    """
    return [')', ')', ')', '('] habitually seen as a single open parenthesis
```