```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    levels = 0
    parentheses = []
    for char in parent_string:
        if char == '(':
            stack.append(levels)
        levels += 1
        if char == ')':
            if levels == 0:
                parentheses.append(stack.pop()
                stack.pop()
            stack
        return parentheses
```

The function `parse_nested_parens` takes a string of nested parentheses as input and returns a list of the deepest levels of nesting parentheses. It uses a nested list to keep track of the depth of each group of parentheses. The function iterates over the string, and for each opening parenthesis, it increments the `levels` counter. When a closing parenthesis is encountered, it checks if the `levels` counter is empty. If it's not empty, the current `stack` is popped from the stack, and the contents are appended to the `parentheses` list. If the `levels` counter is empty, it means that there are no more levels of nesting left, and the function returns the `parentheses` list.

This self-contained function can be used to parse and deepest level of nesting of any given string of parentheses.