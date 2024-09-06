```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], '())':
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

The approach employs a zipper algorithm that matches openers and closers in reverse. Increasing the stack maintains the current nesting level while decreasing updates the level accordingly. To handle multiple groups, we iterate through the string and process each group separately, appending its result to a result list. The zipperless version avoids explicit counters and uses the stack size at the end to indicate the deepest nesting level, providing a more concise solution.