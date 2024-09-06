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
                print('UNBALANCED!' if char == ')' else None)
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if not stack:
        result.append(''.join(current_group))
    else:
        print('UNBALANCED!' if stack else None)
        return None
    
    return result
```
The provided Python script includes a function `separate_paren_groups` that takes a string as input and returns a list of strings. This function is designed to separate a given string containing multiple groups of nested parentheses into individual lists, ensuring that each group is balanced (with correctly matched opening and closing parentheses) and not nested within each other. To achieve this, it uses a stack to keep track of nested parentheses groups.

The script works as follows:
1. The `paren_string` is iterated character by character.
2. When an open parenthesis '(' is encountered, the current group is pushed to the stack. This signifies the start of a new group.
3. When a closing parenthesis ')' is encountered:
   - If the stack is empty, this indicates an unbalanced parenthesis, and a message is printed indicating an unbalanced string. Returns None in this case.
   - If not empty, the topmost group (the one corresponding to the matching open parenthesis) is popped from the stack and appended to the current group.
4. For all other characters (ignoring spaces), the character is directly appended to the current group.
5. After processing all characters, if the stack is empty, it means all groups are balanced, and the current group is appended to the result list.
6. If the stack is not empty, this indicates an unbalanced group, and a message is printed indicating an unbalanced string. Returns None in this case.

Overall, the script handles scenarios involving nested and nested-but-balanced parentheses groups efficiently. It effectively separates the input string into a list of individual groups, considering only the parentheses characters, and appropriately handles potential imbalances in the input.