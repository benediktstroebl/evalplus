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
                print('WRONG ANSWER')
                return None
            current_group.append(char)
            top_group = stack.pop()
            if not stack:
                result.append(')'.join(current_group))
            else:
                stack[-1].append(current_group)
                current_group = top_group
        else:
            current_group.append(char)
            
    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, it pushes the current group onto the stack and starts a new empty group. When a close parentheses `)` is encountered, it checks if the stack is empty. If so, there are unbalanced parentheses and the function returns `None`. 

If not, the function pops the top item from the stack, which is the most recently opened group. It then appends the current group to that group and continues processing. If there are no more groups to process after popping, the current group is the last one and it gets appended to the result list.

The resulting list of strings contains all the balanced parentheses groups from the input string, separated from each other and nested within each other.