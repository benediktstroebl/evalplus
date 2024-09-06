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
                stack.append(level)
        result.append(stack.pop())
    return result
```

The approach employs a counter `level` to monitor the current nesting level every time an opening parenthesis is seen. This level is subsequently added to the `stack` to be reversed later to obtain the maximum depth of nesting. Consequently, the final nesting level of each group is registered in the `result` list.