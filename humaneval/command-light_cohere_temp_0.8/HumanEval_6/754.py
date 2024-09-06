```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    levels = 0
    for char in parent_string:
        if char == '(':
            stack.append(levels)
            levels += 1
        elif char == ')':
            if len(stack) == 0:
                raise ValueError("Unclosed group.")
            top_level, _ = stack.pop()
            levels -= 1
            stack.append(levels)
   return stack
```

This function takes a string of nested parentheses and returns a list of the deepest levels of nesting. It uses a stack data structure to keep track of the level of nesting. This way works by incrementing the level with each opening parent and decrementing the level with each closing parent.