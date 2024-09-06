Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
            if stack:
                current_group = stack.pop()
            else:
                print("Unexpected right parenthesis")
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack to keep track of nested parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. When a close parenthesis is encountered, it checks if the stack is empty or not. If the stack is not empty, the script pops the top group from the stack, indicating the end of the nested set of parentheses, and appends it to the `result` list. The script also handles the case where there are extra closing parentheses.

When the loop is finished, any remaining items in the current_group are added to the result since they cannot be nested within any closing parentheses. The function returns a list of strings representing the separate groups of parentheses.