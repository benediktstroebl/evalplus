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
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The code process each group of parentheses separately, it iterates over each character of a chunk and maintains a stack of open parentheses using a simple incrementer for nesting level whenever an open parenthesis is encountered and a decrementer whenever a close parenthesis is encountered.