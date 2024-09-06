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

The code uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group. It iterates through the characters of the input string, when encountering an open parenthesis, the current group is added to the stack and a new empty group is created. When encountering a close parenthesis, the code checks if it is the closing parenthesis of the last group or a nested group. The current group is yielded when it is the last group or when it is balanced and the stack is empty. The same process is repeated for the nested groups. The current group is appended with the closing parenthesis and yielded. The stack is checked to see if the last group was empty, and if so, it is popped from the stack. If it was not empty, the top of the stack is assigned to the current group variable and popped. This process continues until all the groups in the string are separated and yielded.