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
                return []
            top_group = stack.pop()
            if not top_group:
                result.append(current_group)
            else:
                current_group = top_group + current_group
        else:
            current_group += char

    # handle the last group
    if stack:
        top_group = stack.pop()
        if not top_group:
            result.append(current_group)
        else:
            current_group = top_group + current_group
        if stack:
            return []
    elif current_group:
        result.append(current_group)
    
    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and builds corresponding closed parentheses `)` into strings. It iterates through the input string, pushing each open parentheses onto the stack, and building the current group. When a closing parenthesis is encountered, the algorithm checks if the stack is empty; if so, an unbalanced group is detected, and the function returns an empty list. Otherwise, the algorithm pops the top group from the stack, combines it with the current group, and repeats this process until all groups are processed. The final list of string groups is returned. 

This approach ensures that groups are correctly separated and balanced, and it handles cases where groups are nested or have varying lengths.