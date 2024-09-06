Here is a self-contained Python script that solves the problem of finding the deepest level of nesting for parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_levels: List[int] = [0, 2]
    closing_levels: List[int] = [0, 3]

    for level, char in enumerate(s, 1):
        if char == '(':
            stack.append(opening_levels[level])
        elif char == ')':
            stack.append(closing_levels[level])
        else:
            if stack:
                stack.pop()

   max_level = stack[-1]
                if max_level >= closing_levels[level]:
                    stack.append(opening_levels[level])
                else:
                    return [level]

    return stack
```