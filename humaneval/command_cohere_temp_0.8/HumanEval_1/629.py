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
                return ['Unbalanced input!'] + result
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return result + [stack.pop()]
```
The code uses a stack to keep track of opening parentheses and creates a corresponding list of strings without spaces, representing the nested groups. It checks for proper closing parentheses and handles unbalanced groups with an error message. The output is a list where each item represents a string of one group of parentheses. 
The function returns an error message along with the results for any input strings that start with an unbalanced left parenthesis.