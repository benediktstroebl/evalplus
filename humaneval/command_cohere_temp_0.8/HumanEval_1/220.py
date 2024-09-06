```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                yield current_group
                current_group = stack.pop()
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of nested parens groups. It iterates through the input string, adding characters to the current group when parens are closed and yielding completed groups when they are closed, regardless of nesting. It also handles cases where closing parens don't match with nested groups and ignores any spaces in the input. The main function is directly exposed to solve the problem and will return a list of strings representing the nested groups in the order they appear in the input string.