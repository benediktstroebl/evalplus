```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')':
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a stack to keep track of the depth for each opening parenthesis encountered. The stack is initialized with a depth of 0 for the first opening parenthesis. It increments the top of the stack each time an opening parenthesis is encountered and decrements the stack for each closing parenthesis. The final depth is determined by the last value in the stack after processing the entire string.