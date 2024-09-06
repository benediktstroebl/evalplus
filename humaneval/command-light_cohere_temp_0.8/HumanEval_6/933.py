```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes:
        if char == "(":  # Start of a new group
            stack.append(1)
        else:  # End of a group
            if not stack:  # No nested parentheses
                result.append(1)
                elif stack[-1] == 0:  # Only one level of nesting
                    result.append(stack.pop())
                elif stack[-1] > 1:  # More than one level of nesting
                        stack.pop()
                        result.append(stack[-1])
    else:  # Blank space
                pass
        stack.append(char)
    return result
```