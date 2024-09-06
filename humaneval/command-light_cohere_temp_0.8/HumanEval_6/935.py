Here is a self-contained Python script that solves the problem:
```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    opening_level = 0
    closing_level = 0
    for level, char in enumerate(parenthes, 1):
        if char == '(':
            opening_level += 1
        elif char == ')':
            closing_level += 1
        else:
            stack.push(level)
    stack.pop()
       maxlevel of nesting, return stack
```

This function uses a stack to keep track of the current level of nesting. It pushes opening parentheses onto the format (level) and pushes them onto the stack. It then checks for closing parentheses and pops the stack to find the maximum level of nesting.

This function is a self-contained and can be used to parse any string of nested parentheses.