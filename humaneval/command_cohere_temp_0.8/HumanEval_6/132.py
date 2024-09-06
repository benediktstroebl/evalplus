```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.append(level)
        result.append(stack.pop())
    return result
```

The approach employed by the function `parse_nested_parens` is by iterating through each opening and closing parentheses, tracking the level of nesting using a stack data structure, and updating the level accordingly. The final value is the last item in the stack, corresponding to the deepest level of nesting for that particular group.