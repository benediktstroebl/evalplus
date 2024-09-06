```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                result.append(len)
                stack.push(0) = True
            else:
                stack.append(0)
    else: stack.push(1)
    elif c == '(': stack.append(0)
        elif c == ')': stack.append(1)
    else: stack.push(1)
    else: stack.push(1)
    return result
```

This function uses a stack data structure to track levels of opening parentheses. It works by iterating over the string, maintaining a stack of open parentheses. When a close parenthesis is encountered, it checks if the top of the stack is now a parenthesis, in which case it adds a 1 to the top of the stack and pops a 0 to move the stack down. The function returns a result list of the deepest nesting of parentheses found in the input string.