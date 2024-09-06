```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tier in s.split():
        stack = []
        for c in tier:
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
        result.append(len(stack))
    return result
```

This Python script includes a function (`parse_nested_parens`) that takes a string as input and returns a list of deepest levels of nesting of parentheses in each group. The provided examples show how the function can be used and illustrate its behavior for different inputs.