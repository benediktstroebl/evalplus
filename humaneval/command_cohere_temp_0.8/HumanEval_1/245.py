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
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    if not stack:
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses `(` and constructs the corresponding closing parentheses `)`. The string between the pairs of opening and closing parentheses constitutes a group. The code iterates through the characters of the input string, checking if each character is an opening or closing parenthesis. If it's an opening parenthesis, the current group is added to the stack and a new empty group is started. If it's a closing parenthesis, the code checks if the stack is empty. If it's not, the top item (the last open group) is popped from the stack, added to the current group, and the process continues. If the stack is empty, the current group is the last one and it is directly added to the result. Finally, the resulting list of strings is returned, with each item in the list representing a group of parentheses found in the input string. 

Here is an example usage of the function implementing the markdown code block provided:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```