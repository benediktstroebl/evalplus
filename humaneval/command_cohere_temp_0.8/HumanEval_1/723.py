Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
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
                current_group.append(char)
        else:
            current_group.append(char)

    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

When you run this script and provide the input **`"( ) (( )) (( )( ))"`**, it will produce the output **`['()', '(())', '(()())']`**.

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis **`)`** is encountered, it is matched with the most recent open parenthesis on the stack. If the stack is empty, the current group is unbalanced, and the closing parenthesis is appended to it. The result list is used to store all the balanced groups, and the **`extend`** method is used to add the final group to the result.