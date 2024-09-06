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
                print('Warning: Extra closing parenthesis.')
            else:
                current_group.append(char)
                stack.pop()
                if not stack:
                    result.append(''.join(current_group))
                    current_group = stack[-1]
                else:
                    current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```
This Python script takes a parenthesis string as input and returns a list of well-formed and balanced groups of parentheses. It achieves this by iterating through the characters of the input string, maintaining a stack of current groups of parentheses using a stack data structure. 

When an open parenthesis '(' is encountered, the current group is pushed to the stack and a new group is initiated. Upon encountering a closing parenthesis ')', the system checks if the stack is empty. If it isn't, it retrieves the most recent group from the stack, appends the closing parenthesis to it, and removes it from the stack. This ensures that the group is properly closed. If the stack is empty, it indicates an extra closing parenthesis, resulting in a warning. 

The script continues to iterate through the characters, constantly switching between opening and closing parentheses, until the end of the string is reached. Once the iteration is completed, any remaining groups in the stack are added to the result. Ultimately, the algorithm effectively separates the input string into distinct and well-formed groups of parentheses, disregarding any spaces, and returns them as a list. 

Note: This approach assumes that nested or improperly closed parentheses might not be present, hence the warning for an extra closing parenthesis.