```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # Initialize an empty list to store the results
    stack: List[int] = []
    parent_open = False
    levels = 0  # To keep track of the level of nesting

    for char in s:
        if char == '(':
            parent_open = True
        elif char == ')':
            if parent_open:
                stack.push(levels)
                parent_open = False
        else:
            stack.pop()  # raise Exception
        return stack
```