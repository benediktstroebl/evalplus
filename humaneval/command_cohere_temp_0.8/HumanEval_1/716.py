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
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
            if char == ')':
                stack.append(current_group)
                current_group = []
    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. As the algorithm iterates through the input string, it uses a second data structure (an empty list `current_group`) to store the current group of parentheses when a new open parenthesis `(` is encountered. When a corresponding close parenthesis `)` is found, the group is appended to the stack, and the process is repeated. If the stack is empty, it means we've reached the end of a group and should add it to the result. This approach ensures that all parenthesis groups are properly separated and nested within each other.