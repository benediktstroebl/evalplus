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

The approach employed in the function `parse_nested_parens` is iterative and uses a stack to keep track of the level of nesting for each opening parenthesis. It iterates over each character in the string and adjusts the level accordingly by increasing it when encountering an opening parenthesis and decreasing it when meeting a closing parenthesis. The final nesting level is then recorded in the result list and returned.