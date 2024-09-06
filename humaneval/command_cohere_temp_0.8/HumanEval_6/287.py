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
The function processes each group of parentheses separately and uses a stack to keep track of the current nesting level. The `zip('(()')[::-1]` trick provides the pairs of opening and closing parentheses in reverse order. You can pass this function the input string and it will return a list of the deepest level of nesting for each group of parentheses.