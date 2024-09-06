Here's a self-contained Python function that solves the problem you described:
```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function parses a string containing nested parentheses.
    Returns a nested levels of parentheses.
    """ Input to this string is multiple groups for nested parentheses separated by spaces.
    For example, '(()()) ((())) () ((())()())'

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [i for i, _ in map(lambda x: x.split('()'), s.split(' ' ', s))]
```