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

The approach employs a counter `level` to keep track of the current nesting level, and a `stack` to keep track of _maximum depth of nesting observed_ at each position. When encountering an opener `(`, `level` is incremented and the current `level` is pushed into the `stack`. When encountering a closer `)`, `level` is decremented. Additionally, each time the stack is popped, the maximum value among the stack and the current `level` is retained. This max value observed at each position is the desired output for each string segment.