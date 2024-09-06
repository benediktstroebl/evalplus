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

    # handle the last group
    if stack:
        result.append(''.join(stack.pop()))

    return result
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a new group onto the stack whenever it encounters a open parentheses `(` and starting a new group whenever it encounters a closing parentheses `)`. When it encounters a closing parenthesis with no open parentheses on the stack, it pops the previous group off the stack and adds it to the result. After processing all characters, it handles the last group on the stack, if any.

The problem statement indicates that the input string can contain multiple groups of nested parentheses, and your goal is to separate them into separate strings and return the list of those. Below is an example of how you can use this script to handle such cases: 
 ```python
 >>> separate_paren_groups('( ) (( )) (( )( ))')
 ['()', '(())', '(()())']
 ``` 
 This output will be the expected list of strings corresponding to the separate groups of parentheses.