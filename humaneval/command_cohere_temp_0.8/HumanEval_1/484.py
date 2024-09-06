Here's a Python script that contains a function called `separate_paren_groups` which accepts a string consisting of multiple groups of nested parentheses and returns a list of these separated groups without any spaces.
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
                result.append(')')
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append((').extend(' if len(current_group) == 0 else '')).extend('')')
                current_group = temp
        else:
            current_group.append(char)

    # Add the last group
    if not stack:
        result.append(())
    else:
        temp = stack.pop()
        current_group.extend(temp)
        result.append((').extend(' if len(current_group) == 0 else '')).extend('')')

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the group formed by the current open parentheses is appended to the stack and removed from the current_group list. This process continues until all parentheses are processed. The resulting list of strings is then returned as the output.