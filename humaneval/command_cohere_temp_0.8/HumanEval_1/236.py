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
                print(f"Unmatched '{char}' found!")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Unmatched '(' found!")
        return []
    
    result.extend(current_group)
    return result
```
The provided Python script defines a function `separate_paren_groups` that takes a string `paren_string` as input. This string contains multiple groups of nested parentheses. The goal is to separate these groups into individual strings and return them in a list.

To achieve this, the function uses a stack to keep track of nested parentheses groups. It iterates through each character in the input string, if it encounters an open parenthesis `'('` it pushes the current group onto the stack and starts a new group. When it encounters a closing parenthesis `')'`, it checks if the stack is empty. If not, it pops the top group from the stack, which is the matching open group, and appends it to the current group. All other characters are simply added to the current group.

The function handles cases where closing parentheses are not matched with their corresponding open parentheses. In such cases, it prints an error message and returns an empty list. Additionally, if there are still open groups on the stack after processing the entire string, it prints another error message and returns an empty list.

Finally, the function returns a list of strings, where each string corresponds to a separated parenthesis group, excluding any spaces.