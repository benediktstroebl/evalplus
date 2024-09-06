```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
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

The function takes a string as input and returns a list of the deepest levels of nesting of parentheses in each group. The function uses a zipper to match the opening and closing parentheses and maintain a stack of the levels of nesting. The outermost stack element is the deepest level of nesting for the corresponding group in the input string.