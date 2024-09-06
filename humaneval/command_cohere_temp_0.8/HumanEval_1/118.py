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
                print('UNBALANCED!' if char == ')' else None)
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

This Python script takes a string as input and returns a list of strings. Each string in the list represents a balanced group of parentheses found in the input string. The script uses a stack to keep track of the open parentheses until a closing parenthesis ')' is found.

To test this script, modify the test case in the original problem statement to check if the list of strings is as expected.