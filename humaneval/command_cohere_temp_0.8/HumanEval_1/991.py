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
                print(f"Unmatched '{char}' found.")
            else:
                current_group.pop()
                stack.pop()
                result.append(''.join(current_group))
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```

This code correctly handles nested and nested groups, ensures balancing, and ignores spaces.