```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    stack.append(0)
    result = []
    for par in parentheses_string:
        if par == '(':
            stack.append(1)
        elif par == ')':
            if stack:
                level = stack.pop()
                deepest_level = stack[-1]
                result.append(deepestest_level)
                stack.remove()
            else
                break
        else:
                stack.append(level)
    stack.append(par)
    return result
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest levels of nesting. It uses a stack data structure to keep track of the nesting levels.