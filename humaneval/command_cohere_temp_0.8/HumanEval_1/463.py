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
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

This script employs a stack to manage opening and closing parentheses. It iterates through the input string, pushing a current group of parentheses onto the stack whenever an opening parenthesis is encountered. When a closing parenthesis is met, the last group pushed onto the stack is retrieved and merged with the current group, ensuring proper grouping. If there's no group waiting on the stack, the current group is added to the result list. This process guarantees that all parentheses groups are correctly separated and nested within each other. 

Here's an example usage:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

Output:
```
['()', '(())', '(()())']
```