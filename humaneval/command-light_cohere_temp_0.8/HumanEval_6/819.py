```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function aims to parse and return the deepest level of nesting of parentheses in the input string.
    :string could be represented as multiple groups of nested parentheses separated by spaces.
    Returns a shallowest list of parenthesis levels.
    """
    parse_nested_parens('(()()) ((())) () ((()))()())')
    -> [2, 3, 1, 3]
    """
    stack: List[int] = []
    for char in s:
        if char == '(':
            stack.append(0)
        elif char == ')':
            if stack:
                stack.pop()
       
            else:
                return []
    return stack
```