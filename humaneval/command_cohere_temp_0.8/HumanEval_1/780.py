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
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm utilizes a stack to keep track of opening parentheses until it encounters a closing parenthesis. At this point, it checks if an open parenthesis is at the top of the stack; if it is, the loop appends the current group to the last group (which is the top of the stack), then pops the stack. If the stack is empty, that means the current group is fully processed, so it gets appended to the results list. The loop continues processing the string until all groups are extracted. The results list contains all the balanced groups, properly separated and free of nesting.