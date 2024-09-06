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
                current_group.append(char)
                if not stack:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
            
    return result
```
The algorithm utilizes a stack to keep track of nested paren groups. It iterates through the input string, pushing a group onto the stack whenever it encounters an open paren `(`. It also starts a new group whenever it encounters a open paren. When it encounters a close paren `)`, it checks if the current group is empty. If so, it appends an empty string to the result as there is an extra close paren. If not, it checks if the stack is empty. If so, it means an extra close paren `)` was encountered. This situation is also handled by appending an empty string to the result. If there are still groups on the stack, the current group is popped and added to the previous group. This process continues until all groups are processed. The final result is a list of the separate groups, where each group is a string consisting of the characters within that group.