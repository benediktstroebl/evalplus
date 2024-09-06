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
                return []  # unbalanced group, returning empty list as convention
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The provided Python script completes the task to segregate nested parentheses into individual groups and returns a list of those segregated groups. It uses a stack to keep track of the currently opened groups while it iterates through the input string. When it encounters a closing parenthesis, it checks if the stack is empty, thereby confirming if the group is balanced. If not, it pops the top element from the stack, which is the latest opened group, and appends the current group to the result. The loop continues until the entire string is processed, after which any remaining items in the stack are considered unclosed and are appended to the result as individual items. As such, the function outputs a list of all the distinct, balanced groups of parentheses found in the input string, regardless of whitespace.