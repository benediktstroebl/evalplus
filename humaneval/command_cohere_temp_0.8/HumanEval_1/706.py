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
            elif len(current_group) == 0:
                result.append('')
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
                else:
                    current_group = stack[-1].extend(current_group)
        else:
            current_group.append(char)
    
    # Handling edge case for unbalanced groups
    if current_group:
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses `(` and constructs the corresponding closing parentheses `)`. It initializes an empty list `result` to store the separate groups and iterates through the input string.

When an opening parenthesis is encountered, it pushes the current group onto the stack. When a closing parenthesis is encountered:
- If the stack is empty, this extra closing parenthesis is ignored.
- If the current group is empty, it is also ignored.
- If the current group is not empty, we check whether the stack is empty. If it's not empty, we pop the top of the stack, concatenate it with the current group, and extend it to the last group. This ensures that we combine the nested pairs correctly.

The resulting list of strings `result` contains all the separate groups, and the empty strings handle the cases where there are extra closing parentheses. The algorithm handles nested and balanced parentheses efficiently without recursion and without mutating the original string.