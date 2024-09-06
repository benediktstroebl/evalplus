```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nest = []
    for char in s:
        if char == '(':
            stack.append(nest.append(char))
            nest = []
        elif char == ')':
            if not stack or not nest:
                raise ValueError("Unexpected end of string without nested parentheses.")
            stack.pop()
            stack.append(nest.append(char))
            nest = []
    if nest:
        return [len(nest) for nest in stack]
    return []
```