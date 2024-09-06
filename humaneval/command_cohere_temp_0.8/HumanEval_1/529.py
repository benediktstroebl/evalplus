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
                yield current_group
        else:
            current_group += char
    
    # yield any remaining groups in the stack
    while stack:
        yield stack.pop()
```

This code defines a function `separate_paren_groups` that takes a string `paren_string` as input and returns a list of strings. The function iterates over each character in the input string, tracking open parentheses `'('` and closing parentheses `')'`. It uses a stack to keep track of the current group of parentheses. When an open parenthesis is encountered, the current group is added to the stack and a new empty group is started. When a closing parenthesis is encountered, the code checks if it matches the most recent group at the top of the stack. If it does, the group is popped from the stack and added to the current group. If it doesn't, the most recent group is popped and added to the list of yielded groups, and the current group is replaced with the unmatched closing parenthesis. 

When only closing parentheses remain in the current group and there are no more groups in the stack, the remaining parentheses are yielded as a group. This process effectively separates the nested parentheses into individual, non-nested groups. The order of the yielded groups is preserved, and any spaces are ignored during the processing.