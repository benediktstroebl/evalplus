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

The function processes each group of parentheses separately and uses a stack to keep track of the level of nesting. The `zip('(()', '))'`) argument is for iterating over all possible combinations of opening and closing parentheses. The outer loop iterates over these combinations, while the inner loop uses the stack to keep track of the nesting level and updates it accordingly. Finally, the deepest level of nesting for each group is appended to the result list.