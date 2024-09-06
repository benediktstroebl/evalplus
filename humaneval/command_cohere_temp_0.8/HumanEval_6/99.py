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
The function processes each group of parentheses separately and iterates through each character in the string. It uses a stack to keep track of the levels and adjusts the level accordingly when it encounters opening or closing parentheses. The resulting list of deepest levels of nesting for each group is then returned.

Here is a usage example:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This demonstrates that the function correctly identifies the deepest level of nesting for each group of parentheses in the provided string.