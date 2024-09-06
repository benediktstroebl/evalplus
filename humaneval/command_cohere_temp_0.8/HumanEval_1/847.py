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
                result.append(''.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm utilizes a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, it is added to the stack, and a new group is created. Upon encountering a closing parenthesis `)`, the stack is checked. If it is empty, the current group is added to the result as a final string. If it contains elements, the topmost element (the most recently added group) is popped and added to the current group, ensuring proper grouping. This process continues until all parentheses are processed.

The result list contains the separated string groups in the order they appeared in the input string, without any nesting or unbalanced parentheses. The problem is effectively solved without the use of exceptions, making the code more robust and efficient.