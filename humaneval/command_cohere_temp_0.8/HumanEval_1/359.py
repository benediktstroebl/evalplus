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
                print('UNMATCHED RIGHT PARENTHESIS')
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

The algorithm utilizes a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. It shifts the current group onto the stack upon encountering a new opening parenthesis. This allows us to retain a clean current group to hold the characters between parenthesis pairs. Upon encountering a closing parenthesis, the algorithm checks if the stack is empty, printing a message if it is. If it's not empty, the top element is shifted back to the current group, and the stack is popped to indicate the completion of a group. Finally, the algorithm extends the result list to include all the shifted groups, effectively separating the groups of parentheses. 

The previous and correct approach to this problem was incorrect in its description of the stacking process in the loop. This has now been corrected to more accurately reflect the approach's intended logic.