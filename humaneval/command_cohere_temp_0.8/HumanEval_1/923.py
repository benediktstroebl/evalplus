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

The algorithm utilizes a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to store the closed parentheses `)` and the characters between them. As the algorithm iterates through the input string, it checks the type of character encountered and performs the following:
- If it encounters an open parenthesis `(`, it pushes the current group onto the stack and starts a new group.
- If it encounters a closed parenthesis `)`, it checks if the stack is empty or if the top of the stack is empty. If yes, it appends an empty string to the result list. If not, it pops the top group from the stack, appends the closing parenthesis to the group, and checks if the stack is empty again. If so, it adds the joined string of the current group to the result list.
- If it encounters any character other than a space, it adds the character to the current group.

In this way, the algorithm effectively separates the input string into distinct parentheses groups and ignores any empty strings formed due to unbalanced parentheses.