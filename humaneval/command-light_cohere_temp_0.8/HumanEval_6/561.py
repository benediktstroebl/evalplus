```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string containing multiple groups of nested parentheses separated by spaces as input and returns a list of their deepest nested levels.
    For example, '(()()) ((())) () ((())()())' will return [2, 3, 1, 3].
    """
    stack = []
    for par in s:
        if par == '(':
            stack.append(1)
        elif par == ')':
            if stack:
                stack.pop()
            else:
                return []
    return stack
```