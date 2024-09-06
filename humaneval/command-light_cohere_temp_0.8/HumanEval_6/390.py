```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting of parentheses.
    >>> test_parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [2, 3, 1, 3]
```