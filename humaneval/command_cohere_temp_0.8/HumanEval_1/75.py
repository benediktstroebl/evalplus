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
                return []  # unbalanced group, return an empty list
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code uses a stack to keep track of opening brackets ('(') and builds a corresponding list of strings to hold the nested groups. When a closing bracket (')') is encountered, the stack is checked to ensure it contains an opening bracket of the same depth. If not, an empty list is returned to handle unbalanced groups. Otherwise, the stack is popped to obtain the correct group, which is then added to the result list. Finally, any remaining items in the stack (i.e., unclosed groups) are added to the result as well. Thus, the function handles nested and balanced parentheses groups in the input string and provides a list of separate strings for each group.