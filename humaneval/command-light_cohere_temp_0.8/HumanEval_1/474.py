```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []
    for char in s:
        if char == '(': stack.push(')
        opened = True
        elif char == ')':
            if stack.pop() == '(':
                result.push(') ' + stack.pop()
                pop()
            closed = True
            else:
                stack.push(') ' + char)
        elif char == ' ':
            stack.append(char)
    else: stack.push(char)
    return result
```
This function is designed to take a string of parentheses as input, where each opening parenthesis is considered as the start of a new group and each closing parenthesis as the end of a new group. The function will return a list of separate strings, each representing a group of parentheses.