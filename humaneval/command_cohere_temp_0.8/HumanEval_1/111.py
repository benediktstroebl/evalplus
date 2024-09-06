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
                print("UNMATCHED RIGHT PARENTHESES!")
            else:
                popped_group = stack.pop()
                current_group.extend(popped_group)
        else:
            current_group.append(char)

    if stack:
        print("UNMATCHED LEFT PARENTHESES!")
    else:
        result.extend(stack)
        result.extend(current_group)

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group`
to store the captured content between the parentheses. When a closing parenthesis `)` is encountered, the stack is
checked to ensure that an open parenthesis was previously pushed. If there is an imbalance, an error message is printed. 
The final result is returned as a list, where the collected groups are separated by the order of their appearance in the input string. 
This approach allows the function to properly resolve multiple groups of parentheses and return them as a list of separate strings.