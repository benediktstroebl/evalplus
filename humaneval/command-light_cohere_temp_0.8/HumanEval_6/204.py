```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_parens = ['(', ')', '{', '[', '(']
    closing_parens = [')', ')', '}', ']', ']']

    for char in s:
        if char in opening_parens:
            stack.append(char)
        elif char in closing_parens:
            if stack:
                opening, closing = stack.pop()
                if len(stack) > 0:
                    opening_level = stack.pop()
                    max_level = 0
                    if opening_level > max_level:
                        return [max_level, closing_level, opening_level]
                    else:
                        return []
```