```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[-1], '())':
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

The approach employs a simple algorithm that uses two variables (`opener` and `closer`) to represent the open and close parentheses respectively. It iterates over the string and adjusts the `level` variable accordingly. A stack is used to track the maximum depth of nesting for each group of parentheses. The final result is the list of maximum depths for each group.  This algorithm optimizes its space requirements to O(1) with respect to the string's length.