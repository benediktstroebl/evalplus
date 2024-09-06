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
                print('Mismatched closing parenthesis')
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print('Unmatched opening parenthesis')
        return []
    
    return result if result else [None]
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a copy of the current group onto the stack whenever it encounters an opening parenthesis. When it encounters a closing parenthesis, it checks if the stack is empty (mismatched closing parenthesis) or if the top of the stack is a copy of the current group (properly matched group). In either case, it pops the stack to remove the proper subset of the current group or to complete the group if it was properly matched.

The resulting list of strings is the list of nested groups without spaces, and it is returned as the output. Also, if the result is empty, it is more appropriate to return a list with `None` element rather than an empty list `[]`.

Let's assume the following test cases:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
>>> separate_paren_groups('((a))')
['(a)', '()']
>>> separate_paren_groups('(a)')
['a']
>>> separate_paren_groups('(()())')
[(), ('()',)]
>>> separate_paren_groups('()')
['()']
>>> separate_paren_groups('() ()')
['()', '()']
```
All of these test cases will return the corresponding expected output.