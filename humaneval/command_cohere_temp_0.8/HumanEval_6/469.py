```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        stack = []
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The specified Python script solves the problem using a **stack-based** approach. It converts the token into a string and uses the parentheses '(' ')' to adjust the **level** variable.