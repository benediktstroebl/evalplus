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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    # handle the last group
    if stack:
        print(f"Invalid input - missing closing brace found.")
        return []
    else:
        result.append(''.join(current_group))
            
    return result
```
The algorithm uses a stack to keep track of open parentheses and creates a corresponding list of strings without nested or unbalanced parentheses. Each string in the list represents a separate group of parentheses.