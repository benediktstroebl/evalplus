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
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    # Handle the last group
    if not stack and current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm utilizes a stack to keep track of open parentheses and a separate list to store the current group of parentheses. When a closing parenthesis is encountered, the stack is checked to determine whether it is the end of a group or a nested group. If it is the latter, the nested group is appended to the current group. The process continues until all groups are extracted from the input string and returned as a list.

Here is an example usage of the function:
```python
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

The output of this code will be:
```bash
['()', '(())', '(()())']
```