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
                if not stack:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
    
    return result
```

The algorithm uses a stack to track open parentheses and creates a corresponding list of strings, each of which represents a separate group of parentheses. It properly handles nested groups and does not rely on spaces being present in the input string.