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
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Invalid input - unclosed parentheses.")
        return []
    
    result.append(''.join(current_group))
    
    return result
```
The algorithm uses a stack to keep track of opening parentheses and creates a corresponding list of strings. Once the stack is empty, the algorithm has closed all parentheses, and the final list of strings is returned.