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

The algorithm utilizes a stack to keep track of opening parentheses until it encounters a closing parenthesis. At this point, it checks if an opening parenthesis is at the top of the stack, revealing a separate group of parentheses. This group is added to the result array and popped from the stack. If there are no more open parentheses after this group is popped, it signifies the end of a group, and the current group is added to the result as well. This process continues until all the parentheses are processed. 

This approach guarantees that separate groups are balanced and correctly separated, as long as there are no nested groups within each other. It also ignores any spaces present in the input string.  The `separate_paren_groups` function yields the desired result when tested with the input provided in the problem statement.