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
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group.append(char)
                if not stack:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
            
    return result
```

This Python script takes a string of parentheses and returns a list of strings. Each string in the list represents a separate group of nested parentheses within the input string. The script ensures that the parentheses are balanced and not nested within each other by using a stack data structure. 

To correctly assign each parenthesis pair to their owning group, the approach is to maintain a stack (typeof list) and a current group (typeof list). A group is appended to the result list and the stack is popped when a closing parenthesis ')' is encountered. This guarantees that the groups remain separate and aren't nested within each other. 

The function takes a string as input and returns a list of strings containing the separated parenthesis groups. If you require further clarification on any of the approaches or implementations, please don't hesitate to ask!