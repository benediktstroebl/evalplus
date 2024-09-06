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
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group.append(char)
                if not stack:
                    result.append(''.join(current_group))
        elif char != ' ':
            current_group.append(char)
            
    return result
```
The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings where each element represents a balanced group of parentheses. It initializes an empty list to store the resultant separated groups. Then, it iterates through each character of the input string, leaving spaces out. 

If the character is an open parenthesis, it pushes the current group onto the stack. If it is a closing parenthesis, it checks if the stack is empty, and if so, appends an empty string to the result to account for any unnecessary parentheses, or if not, pops the top group from the stack, appends the closing parenthesis, and checks if the current group is fully closed. If it is, it appends the group to the result. Throughout the loop, current_group keeps track of the current balanced group, ignoring spaces. The result is a list of strings, where each string represents a balanced group of parentheses, without any nesting or unbalanced braces.