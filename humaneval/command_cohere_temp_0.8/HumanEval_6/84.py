```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        stack = []
        level = 0
        for c in chunk:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into chunks where each chunk represents a group of parentheses separated by spaces. It uses a stack to keep track of parentheses openings and calculate the deepest level of nesting for each group. The result is a list where each element represents the maximum nesting level of parentheses in the corresponding group.