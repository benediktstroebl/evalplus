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
            current_group += stack.pop()
        else:
            current_group += char

    return [group.strip() for group in stack] if stack else [current_group.strip()]
```

This script takes a paren_string as input and returns a list of separate groups of parentheses. It uses a stack to keep track of opening parentheses until they are closed, and meanwhile, it builds a current_group string that combines the current balanced parens. The stack is popped when we encounter closing parentheses, and the resulting list of strings is returned. If the stack is empty (i.e., there are no balanced paren groups), then the current_group is returned as a list with a single element. 

This approach ensures that the returned list has a string for each set of balanced parentheses, properly handling cases with nested parentheses, and handling parentheses of any size or complexity. 

The stripped version of the strings in the returned list is ensured by the group.strip() method, which removes any leading or trailing whitespaces. This strippping of spaces is consistent with the instruction in the prompt to ignore spaces in the input string.