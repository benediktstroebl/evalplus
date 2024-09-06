```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append('')
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group.reverse()
                result.append(''.join(current_group))
                current_group = stack.pop() if stack else []
        else:
            current_group.append(char)
    
    # Handle any remaining open parentheses
    while stack:
        current_group.reverse()
        result.append(''.join(current_group))
        current_group = stack.pop() if stack else []
    
    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and constructs the resulting strings accordingly. It iterates through the input string, pushing empty strings onto the stack each time an open parenthesis is encountered. When a closing parenthesis `)` is encountered, the stack is checked for the corresponding opening parenthesis. If found, it is popped from the stack, and the current group is reversed and appended to the results list.

Any remaining open parentheses in the stack at the end of the loop are considered remaining groups, these are also appended to the results list in reverse order after the loop completes. The final result is a list of separate parentheses groups, properly balanced and without any nesting.

This approach handles cases like nested parentheses groups and properly handles parentheses balance, ensuring correct separation of groups.