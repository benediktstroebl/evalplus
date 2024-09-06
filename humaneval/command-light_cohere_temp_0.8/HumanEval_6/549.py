```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns a list of the deepest nesting level.
    Test cases are
    usage:
    ```python
    result = parse_nested_parens('(()()) ((())) () ((()))()')
    assert parse_nested_parens('(()()) ((())) () ((()))()') == [2, 3, 1, 3]
    ```
   
```