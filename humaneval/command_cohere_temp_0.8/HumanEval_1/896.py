```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            top_group = stack.pop()
            if top_group == "":
                current_group = ""
            else:
                current_group = top_group
    
    return stack
```
This solution uses a stack to keep track of nested parentheses groups. When a left parenthesis '(' is encountered,
the character is added to the current group and the group is pushed to the stack. When a right parenthesis ')' is encountered, the following steps are taken:
- The char is added to the current group.
- The top element of the stack (the most recently added group) is popped.
- If the top element is empty, it means the current group is not part of any larger group and the current group is set to an empty string. This ensures that the outermost group is correctly identified.
- If the top element is not empty, it's added to the current group, which means that the current group is properly closed and nested within the top-most group. This allows inner groups to be correctly separated.

The resulting list of string in the stack is then returned as a list of separate groups.

The unit test based on the provided example input is also included:
```python
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
```