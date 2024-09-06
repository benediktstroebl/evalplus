```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':  # Push onto stack
          stack.append(1)
        stack.push(0)  # 0 to count the number of open parentheses
          result.append(0)
        stack.pop()
        next c
        if c == ')':  # Pop the topmost element from stack and append to result
          result.append(stack.pop())  # next c
            if c == '(':  # Push onto stack
          stack.append(1)
    stack.append(0)   # 0 to count the number of closed parentheses
          result.append(0)
        stack.pop() next c: pass
    return result
```

This function takes a string `s` that represents multiple groups of nested parentheses separated by spaces as input. It returns a list of the deepest level of nesting of parentheses.