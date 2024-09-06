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

The algorithm utilizes a stack to keep track of opening parentheses until it encounters a closing parenthesis.

At that point, it checks if the closing parenthesis corresponds to the top element in the stack (meaning they form a balanced group), or if it closes a group that was nested within the current one. In both cases, it removes the relevant entries from the stack and adds the balanced group to the results.

The script ignores any spaces in the input string and returns a list of separate groups of parentheses.