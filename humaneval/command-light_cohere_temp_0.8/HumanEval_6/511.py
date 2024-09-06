```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for a given string of parentheses.
    Input:
    parent_string - A string that represents multiple groups of parentheses, separated by spaces.
    Returns:
    list of the deepest level of nesting for each group of parentheses.
    """

Example usage:
    ```python
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(() () ))()') == [2, 3]
    ```
```