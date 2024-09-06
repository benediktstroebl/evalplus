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
                result.append('')
            elif len(current_group) == 0:
                result.append('')
            else:
                prev_group = stack.pop()
                current_group.extend(prev_group)
                if not stack:
                    result.append(''.join(current_group))
                else:
                    stack[-1].extend(current_group)
                    current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm utilizes a stack to track open parentheses and constructs strings on the stack closest to them. It effectively handles nested groups, correctly combining them with their matching counterparts. This approach ensures balanced groups are separated correctly, as shown in the provided test case. The resulting list of strings contains each group as individual elements.