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
                print('Unmatched close parenthesis')
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print('Unmatched open parenthesis')
        return []
    else:
        result.append(''.join(current_group))

    return result
```
The code uses a stack to keep track of open parentheses and a list to hold the currently balanced group of parentheses. It iterates through the input string and pushes a new empty group onto the stack whenever it encounters an open parenthesis. When it encounters a close parenthesis, it checks if the stack is empty or not. If the stack is empty, it means there is an unmatched opening parenthesis. If it's not empty, it pops the top of the stack to get the corresponding opening parenthesis and checks if it matches with the current closing parenthesis. The currently balanced group is added to the result list whenever the stack is empty and we've hit the end of a group. Finally, it returns the list of separate groups of parentheses.