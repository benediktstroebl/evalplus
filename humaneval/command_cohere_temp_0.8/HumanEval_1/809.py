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
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. Then it checks if the current group is empty, in which case the closing parenthesis is appended to the result, or the content of the current group is added to the stack. This allows us to recover the nested structure of parentheses in the string and print it as a list of balanced groups. The spaces are ignored as per the instructions.