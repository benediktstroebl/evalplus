```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tok in s.split():
        level = 0
        stack = []
        for c in tok:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The code uses a stack to track the opening parentheses encountered while iterating over each token in the input string. The `level` variable keeps track of the current depth of nesting, which is incremented each time an opening parenthesis is added to the stack, and decremented each time a closing parenthesis is removed from the stack. The function returns a list where each element corresponds to the deepest level of nesting encountered in each token separated by spaces.