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
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```

This Python script uses a stack to keep track of nested paren groups. It iterates through the input string, appending to the current group when it encounters a punctuation mark other than `)`. When it encounters a open parentheses `(`, it pushes the current group to the stack and starts a new group. When it encounters a close parentheses `)`, it checks if the stack is empty. If so, there's an unbalanced parenthesis, and the function returns an empty list.

If the stack is not empty, the function checks if the top of the stack is empty. If not, it pops the last group and appends it to the current group. This allows nested groups to be properly handled. If the top of the stack _is_ empty, then the current group is the last group, and it's added to the result list and popped from the stack.

The result list of properly separated and nested groups is then returned.