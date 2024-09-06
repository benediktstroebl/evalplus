```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    results = []
    for t in s:
        if t == '(': stack.append(0)
        elif t == ')':
            if stack:
                results.append(stack.pop()
            a clarity = 1 if len(stack) == 1 else 0)
                stack.clear()
        clear_stack = 1 if len(stack) == 2 else 0
            stack.append(clear_stack)
        elif t == '()':
            if stack:
                results.append(stack.pop()
                clarity = 2 if len(stack) == 2 else 1)
                stack.clear()
    cleared_stack = 1 if len(stack) == 3 else 0
            stack.append(cleared_stack)
        else:
            stack.append(t)
    return results
```

This Python function named `parse_nested_parens` takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. It uses a stack to keep track of opening parentheses.