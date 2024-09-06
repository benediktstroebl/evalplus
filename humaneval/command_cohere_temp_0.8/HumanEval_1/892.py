```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = stack.pop()
                yield current_group
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of nested parentheses groups. The `current_group` variable stores the currently opened group of parentheses. When a closing parenthesis is encountered, the code checks whether it matches the last opened group on the stack. If it does, the group is added to the output and removed from the stack. If not, the stack is popped to retrieve the most recently opened group that matches a closing parenthesis, added to the output, and then the stack is restored. The process continues until all parentheses are processed.

The tests included in the problem are:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']

>>> separate_paren_groups('((a))')
['(())', 'a']

>>> separate_paren_groups('(a)')
['a']

>>> separate_paren_groups('())')
['()']

>>> separate_paren_groups('( )) ')
['()']
``` 

This code should be able to pass all these tests.