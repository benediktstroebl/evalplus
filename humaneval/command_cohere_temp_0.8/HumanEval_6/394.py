```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a stack to monitor the depth of nesting for each group of parentheses. The stack is initialized to zero and every time a closing parenthesis is encountered, the corresponding value is popped off the stack, updating the result. To handle multiple groups of parentheses separated by spaces, the algorithm is iterated through each group, using the space character as a separator.