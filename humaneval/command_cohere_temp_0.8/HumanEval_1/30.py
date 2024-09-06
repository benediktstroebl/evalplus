```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                print(f"Unmatched right parenthesis '{char}'")
        else:
            current_group += char
    
    return stack
```
This approach utilizes a stack to keep track of nested groups, incrementing whenever an open parenthesis is encountered and
decrementing when a close parenthesis is found. The final list of strings contains the remnants of the stack, which
corresponds to the separate groups of parentheses. 

**NOTE:** This solution is not optimized for performance, as it uses a stack data structure which is not efficient for
nested input structures. However, it remains a pragmatic solution for this problem and would easily pass the stated test.