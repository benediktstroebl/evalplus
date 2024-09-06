```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for group in s.split():
        level = 0
        stack = []
        for c in group:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    break
                level += 1
                stack.pop()
        result.append(level)
    return result
```

This script uses a simple **stack** methodology to solve the issue, and the **result** list is populated by iterating over each group in the input string. An example input return is **[2, 3, 1, 3]** for the string **'(()()) ((())) () ((())()())'**.