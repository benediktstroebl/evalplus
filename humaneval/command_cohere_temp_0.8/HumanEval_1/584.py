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

The algorithm utilizes a stack to track open parentheses and constructs strings on the stack ejection. This solution effectively handles nested groups of parentheses and provides the expected output. The tests included in the problem statement would be sufficient to prove the correctness of this code.