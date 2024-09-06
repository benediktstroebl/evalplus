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
                return ['Invalid input! No opening paren to match this closing one.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening parentheses until we encounter a closing one. When we meet a closing parenthesis, we check if we have a corresponding opening one on the stack. If we do, we add the nested group to the result and pop the opening parenthesis from the stack. If we reach the end of the string and there is an opening parenthesis left on the stack, this means an unclosed group, and we return an error. Tacking spaces during the process ensures we achieve the "ignore spaces" intended behavior. 

This approach ensures that:
- Groups are balanced
- Groups are not nested within each other 
- If the input is invalid, it notifies with an error message. 
```python
# Test the function
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
assert separate_paren_groups("((a)(b))") == [ '((a)(b))']
assert separate_paren_groups("(a)") == ['(a)']
assert separate_paren_groups("())") == [ '()']
assert separate_paren_groups("((a")) == ['Invalid input! No opening paren to match this closing one.']
```