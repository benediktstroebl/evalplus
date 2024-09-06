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
                current_group = stack.pop()
    else:
        yield current_group
```

The algorithm utilizes a stack to keep track of open parentheses `(` and builds corresponding strings of closed
parentheses. When it encounters a closing parenthesis `)`, it checks whether it has a matching open parenthesis
at the top of the stack. If it does not, the current string is yielded. This way, the function achieves the goal
of separating groups of parentheses and yields each separate group as a string, regardless of nesting levels
and resulting lengths of each group.  It ignores any spaces present in the input string for the sake of
grouping semantics only.