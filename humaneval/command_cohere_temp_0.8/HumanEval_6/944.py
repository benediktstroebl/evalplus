```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        level = 0
        stack = []
        for c in chunk:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    break
                stack.pop()
            if len(stack) == 0:
                level += 1
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest nesting level of parentheses in each substring split by spaces. It utilizes a stack to track the nesting level and increments the level when the opening parentheses outweigh the closing parentheses in a chunk.