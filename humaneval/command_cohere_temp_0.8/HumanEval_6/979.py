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
            elif c == closer:
                level = stack.pop()
                if stack:
                    result.append(max(stack))
            else:
                level += 1
        if stack:
            result.append(max(stack))
    return result
```

The approach employs a simple algorithm that uses two stacks -- one for keeping track of the current parentheses level, and another to track the maximum depth reached so far. When an opener is encountered, it is added to the first stack, and the second stack is checked to see if the current depth is already greater than the maximum. If so, the maximum is updated. A closer is processed by popping the first stack to check the current depth and updating the maximum as necessary. All other characters simply increment the current depth.