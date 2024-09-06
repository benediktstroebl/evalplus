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
                current_group = []
        else:
            current_group.append(char)
    
    # Handle any remaining groups
    while stack:
        if not stack[-1]:
            result.append('')
        else:
            stack.pop()
            current_group.reverse()
            result.append(''.join(current_group))
        current_group = []
    
    return result
```
The algorithm uses a stack to keep track of the current nested parens and a separate list to store the concatenated contents of each group. As it iterates through the input string, it pushes a ')' onto the stack whenever it encounters a '(' and vice versa. When it encounters a ')' without an intervening '(' (indicating the end of a group), it checks if the stack is empty or contains a empty string (indicating the end of a group). If so, it pops the top of the stack, reverses the contents of the current group, and adds it to the result list. Any remaining ')' that aren't matched by a '(' are treated as standalone groups, so they are popped and added to the result as well. This algorithm assumes that there are no nested groups and thus doesn't need to handle nested parentheses beyond the current implementation.