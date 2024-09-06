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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print(f"Invalid input - unclosed brace")
        return []
    else:
        result.append(''.join(current_group))

    return result

# Example input
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
``` 

This script uses a stack to keep track of nested paren groups. It iterates through the input string, pushing each open paren onto the stack and collecting the characters between each open and close paren into `current_group`. When a close paren is encountered, the topmost open paren on the stack is popped and added to `current_group`. Any remaining open parentheses indicate an incomplete group, so the function prints an error message and returns an empty list if this situation is detected. Finally, all the completed groups are appended to the `result` list and returned.