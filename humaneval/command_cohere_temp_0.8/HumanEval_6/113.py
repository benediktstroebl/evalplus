```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [0]
        stack = [0]
        for char in segment:
            if char == '(':
                stack.append(open_brackets[-1]+1)
                open_brackets.append(stack[-1]+1)
            elif char == ')':
                open_brackets.pop()
                stack.pop()
        result.append(max(open_brackets))
    return result
```