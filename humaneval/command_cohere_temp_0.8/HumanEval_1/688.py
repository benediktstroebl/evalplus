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
                print(f"Unmatched '{char}' found")
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Group balancing error: {stack}")
        return None
    
    result.append("".join(current_group))
    
    return result
```
The provided code incorporates a **'stack'** data structure to efficiently keep track of the parenthesis balances. When a closing parenthesis is encountered, the system checks if the corresponding opening parenthesis is present on the stack. If it is, the opening parenthesis is popped from the stack, and the two parentheses are considered paired. If the opening parenthesis is not found on the stack, it signifies an unbalanced set of parentheses, and the function returns 'None' to represent failure. Additionally, the code takes into account nested groups of parentheses.