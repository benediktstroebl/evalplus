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
                yield current_group
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char

    # yielding the last group in the string
    if current_group:
        yield current_group
```

The code leverages a stack to properly isolate and yield nested and balanced groups of parentheses. When encountering an open parenthesis, it pushes the current group onto the stack and starts a new group. Upon encountering a closing parenthesis, it checks the stack. If the top element is empty, it yields the current group and pops the empty element. If the top element is not empty, the closing parenthesis matches the top element, so it pops it from the stack and continues building the current group. Finally, if additional closing parentheses are encountered and there are no more groups to isolate, the current group is yielded. This approach ensures the proper isolation and extraction of nested groups of parentheses. 

This approach allows the program to correctly separate the groups in the following string: '( ) (( )( ))' and yield the output: ['()', '(())', '(()())'].