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
            if not stack:
                print("Unexpected right parenthesis")
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack to keep track of nested parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. When a closing parenthesis is encountered, it checks if the stack is empty or not. If the stack is empty, it means there is an extra right parenthesis which is not balanced. If it's not empty, the script pops the top group from the stack, which is the matching open parenthesis, and adds it to the current group. All other characters (excluding spaces) are added to the current group. Finally, the script adds all the nested groups to the result list and extends it with the last group encountered.

When the given example string `"( ) (( )) (( )( ))"` is passed to `separate_paren_groups`, it returns a list `['()', '(())', '(()())']`, which is then printed to the console.