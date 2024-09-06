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
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employed by the function involves treating each group of parentheses as a separate entity and utilizing a stack to track the level of nesting. Subsequently, the function appends the maximum depth of nesting for each group to the `result` list.