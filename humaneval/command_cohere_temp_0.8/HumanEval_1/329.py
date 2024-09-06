Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing balanced groups of parentheses:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = [0]
    close_braces = [0]
    output = []
    stack = []
    for char in paren_string:
        if char == '(':
            open_braces[0] += 1
        elif char == ')':
            close_braces[0] += 1
        else:
            continue
        if open_braces[0] == close_braces[0]:
            current_group = ''.join(stack)
            stack.clear()
            open_braces[0] = 0
            close_braces[0] = 0
            output.append(current_group)
        else:
            stack.append(char)
    else:
        current_group = ''.join(stack)
        stack.clear()
        output.append(current_group)
    return output

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This script uses a stack to keep track of opened braces as it traverses the input string. When the balance is settled (number of opening and closing braces are equal), the group is added to the output list, and the stack is cleared. The resulting output list contains the separated groups of parentheses.