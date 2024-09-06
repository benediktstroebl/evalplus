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
                yield current_group
                current_group = stack.pop()
        else:
            current_group += char
            
    # Make sure to yield the last group if it was properly closed
    if not stack:
        yield current_group
    elif stack[-1] == current_group:
        yield current_group
```