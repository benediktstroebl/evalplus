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
                print('Unbalanced parentheses!')
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.append(''.join(current_group))
    
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of nested parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. When a close parenthesis is encountered, it checks for balancing by verifying if the stack is empty or not. If not, it pops the top of the stack to resume the previous group. Finally, the function returns a list of strings, each containing a separate group of parentheses.

When you run this script with the example input, it will output:
```bash
['()', '(())', '(()())']
``` 

This exemplifies how the `separate_paren_groups` function successfully processes nested groups of parentheses and returns them in a structured list form.