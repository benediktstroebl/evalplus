Here's the self-contained Python script with a function that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_levels: List[int] = [0, 2]  # 0 for opening () and 2 for closing )

    for c in s:
        if c == ' ':
            stack.append(opening_levels.pop()
        max_level = min(stack)
        elif c == '(':
            stack.append(opening_levels.append(1)
            stack.append(opening_levels.pop())
            opening_levels.append(0)
            stack.append(1)
            stack.append(opening_levels)
        elif c == ')':
            stack.pop()
            deepest_level = min(stack)
            if deepest_level == 0:
                raise ValueError("Unmatched closing parenthesis!")
            elif deepest_level == 2:
                opening_levels.pop()
                if deepest_level == 1:
                    opening_levels.pop()
            return opening_levels
```