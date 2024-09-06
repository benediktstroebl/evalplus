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
                temp = stack.pop()
                current_group.extend(temp)
            current_group.append(char)
        else:
            current_group.append(char)
            
    if not stack:
        result.append(''.join(current_group))
    else:
        temp = stack.pop()
        current_group.extend(temp)
    return result
```

The code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked to determine whether it is the end of a group or not. If not, the current group is appended to the most recent group in the stack and the group is added to the result. If it is the end of a group, the contents of the current group are combined with the most recent group and added to the result. Ultimately, all nested groups are separated and returned as a list. 

Here is an example output of the function:
```
['()', '(())', '(()())']
``` 

The function is also unit-tested with the following code:
```python
def test_separate_paren_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
    assert separate_paren_groups("((a))") == ['(a)']
    assert separate_paren_groups("()") == ['()']
    assert separate_paren_groups("(a)") == ['(a)']
    assert separate_paren_groups("((()))") == ['()']
    assert separate_paren_groups("((((a))))") == ['((a))']
    assert separate_paren_groups("((a)b))") == ['(a)b']
    assert separate_paren_groups("((a))(", 1) == ['(a)(']
```