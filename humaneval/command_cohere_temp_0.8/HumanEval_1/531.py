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
                result.append('')
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group = stack[-1]
        else:
            current_group.append(char)
    
    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This code uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a new group onto the stack whenever it encounters a open parentheses '('. It also starts a new group whenever it encounters a closed parentheses ')' if and only if the stack is not empty and the top element is empty. The code appends the current character to the current group unless it encounters a '(' or a ')' character. Finally, after processing the entire string, the code returns a list of strings, where each string corresponds to a balanced group of parentheses.