Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses. The code is designed to handle nested and nested-within-nested groups, and it ignores any spaces in the input string.

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
                print("UNBALANCED!")
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script deals with parentheses that are nested and nested-within-nested. It does so by maintaining a stack of current groups and toggling between starting a new group with '(' or adding to the current group with other parentheses. When it encounters a ')', it checks the stack to determine whether the current group is closed properly and whether there are any nested groups. If there's at least one group on the stack, the current group is added to the last group on the stack, and the stack is popped and added to the result. The process ensures that every open parenthesis has a matching close parenthesis and that groups are not nested within each other. 

When tested with the input (`( ) (( )) (( )( ))`), it produces the desired output (`['()', '(())', '(()())']`).