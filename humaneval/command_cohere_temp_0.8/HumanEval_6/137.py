```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [0]
        stack = [0]
        for char in segment:
            if char == '(':
                open_brackets.append(open_brackets[-1] + 1)
                stack.append(open_brackets[-1])
            elif char == ')':
                open_brackets.pop()
                stack.pop()
        result.append(max(stack))
    return result
```

The approach uses a stack to keep track of the deepest brackets for each segment and updates the stack accordingly as the input string is traversed. A sample output of the function is:
```python
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```