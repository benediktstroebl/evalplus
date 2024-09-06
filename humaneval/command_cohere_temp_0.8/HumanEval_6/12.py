```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        for c in s:
            if c == opener:
                stack.append(stack[-1] + 1)
            elif c == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a stack to track the difference between opening and closing parentheses. The zip('(()', '))'maps the opening parenthesis '(' to '(()' and the closing parenthesis ')' to '))'. For each character in the string s, the algorithm increments the top of the stack if it's an opening parenthesis and decrements it if it's a closing parenthesis. Finally, the deepest level of nesting for each group is appended to the result list.