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
                return ['Invalid input! No opening parentheses found to match this closing parenthesis.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening parentheses until the matching closing parenthesis is encountered. This ensures we handle nested parentheses correctly, regardless of their positions in the string. Each time we encounter a closing parenthesis, we check if the stack is empty. If it is, the input is invalid, as there's no matching opening parenthesis. If it's not, we pop the top of the stack to obtain the correct group that the opening parenthesis belongs to and append the captured characters to it. Lastly, we handle any trailing opening parentheses by adding them to the stack, ensuring they aren't forgotten. The resulting stack contains each group as a list, which we then convert to strings and return. Thus, the function gracefully handles any spaces in the input string.