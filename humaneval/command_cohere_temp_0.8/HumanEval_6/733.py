```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level = stack.pop()
        result.append(level)
    return result
```
The function processes each group of parentheses separately and uses a stack to keep track of the level of nesting. The `zip('(()')[::-1]` trick provides the pairs of opening and closing parentheses in reverse order. The result is appended to a list of int values that represent the maximum nesting level for each group of parentheses.