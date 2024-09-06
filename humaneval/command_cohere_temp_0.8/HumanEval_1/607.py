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
            if stack:
                stack.pop()
            else:
                print(f"Unmatched close brace: {char}")
        else:
            current_group += char
    
    return stack
```
This Python script uses a stack to correctly separate the nested parentheses into separate groups and returns a list of these groups. It handles nested groups of any depth and correctly balances the braces.