```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes:
        if char == '(':
            stack.append(0)
        elif char == ')':
            if stack:
                result.append(stack.pop()
                open the