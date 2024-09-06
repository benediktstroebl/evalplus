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
                result.append(''.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, we push the current group onto the stack and start a new group. When a closing parentheses `)` is encountered, we first check if we have a stack. If we don't, this closing parenthesis closes the current group, and we append it to the result before resetting the current group. If we do have a stack, we pop the top group from it, extend it into the current group, and then check if the stack is empty. If it is, we append the current group to the result and reset it. Throughout the loop, we simply add every character that is neither an opening nor a closing parenthesis to the current group. The resulting list of strings is the output of the function. 

The unit test based on the example provided in the problem prompt is added to the code for verification:
```python
def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```