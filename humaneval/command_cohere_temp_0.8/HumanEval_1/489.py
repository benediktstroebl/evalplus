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
            else:
                yield from separate_groups_with_nesting(stack, current_group)
                stack = [current_group]
        else:
            current_group += char
    
    if stack:
        yield from separate_groups_with_nesting(stack, current_group)

def separate_groups_with_nesting(stack: List[str], current_group: str) -> List[str]:
    """Yield each separate group in the stack and then the current group."""
    for group in stack:
        yield group
    yield current_group
```