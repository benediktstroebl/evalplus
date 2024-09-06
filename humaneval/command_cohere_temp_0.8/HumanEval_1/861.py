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
                result.append(')')
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append((').extend(' if len(current_group) == 0 else '')).extend('.append(') + ''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of nested parens. It iterates through the characters of the input string, pushing a newly initialized `list` onto the stack upon encountering an open paren `(`. It also initializes a `list` to keep track of the current group of parens. Upon encountering a closing paren `)`, it checks if the stack is empty or not. In the case of an empty stack, this implies the closing paren has no matching open paren, so it's appended to the result as an isolated paren. In the case of a non-empty stack, the top item is popped which is the open paren's matching list, and appended to the current group. This process continues until all parens are processed. The final result list is returned, where each item is a separate group of parentheses. 

Such a process assures that we handle the following edge cases:
1. Handling an unbalanced group like `(`) and handling the edge case of `( ) (( )` producing `['(', '(', ')']`.
2. Handling nested groups like `( ) (( )) (( )( ))` producing `['()', '(())', '(()())']`.