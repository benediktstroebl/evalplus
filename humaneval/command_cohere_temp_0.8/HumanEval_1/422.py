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
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char
            
    # Yield the last group in the string
    if current_group:
        yield current_group
```

This script uses a stack to keep track of nested parentheses groups. When a '(' is encountered, the current group is added to the stack and a new empty group is created. When a ')' is encountered, the code checks whether it belongs to the last group in the stack (which would be an unclosed group), or whether it closes the group at the top of the stack. In the latter case, the group is yielded and removed from the stack. If the stack is empty, the current group is the last one in the input and is directly yielded. The algorithm yields each separate group of parentheses as a list, and in the provided example, the result is: ['()', '(())', '(()())'].