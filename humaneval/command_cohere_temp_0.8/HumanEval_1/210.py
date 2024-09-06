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
                return ['']
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```

The algorithm utilizes a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, it is appended to the `stack` and the `current_group` is reset to an empty list. Upon encountering a closing parenthesis `)`, the following steps are performed:
1.  If the stack is empty, implying an unbalanced parenthesis, return a list with an empty string.
2.  Otherwise, if the top element in the stack is empty, indicate that a group is closed, and the content of the `current_group` is added to the `result` list. Subsequently, the corresponding open parenthesis at the top of the stack is popped to check for more content within the group or to close the outermost group.
3.  In case the top of the stack is not empty, it implies an open parenthesis from an inner nested group. Therefore, the current group is swapped with the top of the stack and the processing continues to track the inner group.

Overall, this algorithm effectively separates the given string into a list of strings based on the balanced parentheses groups.