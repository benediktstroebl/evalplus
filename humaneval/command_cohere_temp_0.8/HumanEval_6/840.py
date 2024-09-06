```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')':
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

The approach employs a counter (level) to keep track of the depth while iterating through the characters of the input string s. When an opener is encountered, the level is incremented, and when a closer is encountered, the level is decremented. Additionally, the maximum depth achieved during each iteration is appended to the list stack. Finally, the maximum depth (deepest level of nesting) for each group is obtained from the stack and appended to the result list.