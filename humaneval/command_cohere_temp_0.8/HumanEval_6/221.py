```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        stack = []
        level = 0
        for c in segment:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The code uses a stack to track the nesting level of parentheses in each segment. It iterates through each character of a segment and adjusts the stack and nesting level accordingly. The nesting level is incremented when the opening parenthesis '(' is encountered and decremented when the closing parenthesis ')' is encountered. The process is repeated for each segment of the input string, and the resulting nesting levels are stored in a list.