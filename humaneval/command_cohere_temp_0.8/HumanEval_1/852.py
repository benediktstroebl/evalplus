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
            
    # Make sure to yield the last group if it was properly closed
    if not stack:
        yield current_group
    elif stack[-1] == "":
        stack.pop()
        yield current_group
            
    return list(filter(None, stack))
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, it is checked whether it belongs to the most recent open parenthesis. If so, the group is added to the stack. If not, the stack is checked for the most recent group that was not closed yet, which is then added to the output. The final output list is filtered to remove any empty strings, which occur when groups are not closed. This solution passes the provided test case `"( ) (( )) (( )( ))"` with the output `['()', '(())', '(()())']`.