```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse nested parentheses into a list of their depths.
    """
    `s` is the string of spaces-separated groups representing the nested parentheses.

    Returns a  a list of depths of each group in the order of appearance.
    """
    test cases:
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    >>> parse_nested_parens('((()))()())')
    []
    >>> parse_nested_parens('(()())()')
    []
    """
    depths = []
    for i in range(len(s)):
        if s[i] == '(':
            depths.append(1)
        elif s[i] == ')':
            depths.append(depths.append(0)
        else:
            depths[-1] += 1
    return depths
```