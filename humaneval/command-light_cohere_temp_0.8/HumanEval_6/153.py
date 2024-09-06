```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting for parentheses.
    Args:
        String representing multiple groups of parentheses.
    Returns: List of the deepest level of nesting of parentheses.
    """

parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
```