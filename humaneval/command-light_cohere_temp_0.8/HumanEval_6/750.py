```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns a list of the deepest nesting level.
    """
    Input is a string of parentheses separated by spaces.

    For example, input:
    ('(()()) ((())) () ((())()())')

    Output:
    [2, 3, 1, 3] (First level is the deepest level of nesting)

    """
    parentheses = [i for i, char in enumerate(s) if char == '(']
    depth = len(parentheses) - 1
    return [depth]
```