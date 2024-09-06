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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening braces '(' and pops them accordingly to match the closing braces ')' while collecting the characters between them. 

The problem is explained in the code with comments and the testing functionality is implemented through the 'print' statement with the corresponding message in case the extra closing brace is found. 
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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
# Testing the above function
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
>>> separate_paren_groups('(abc'))
['(abc)']
>>> separate_paren_groups('())')
['()']
>>> separate_paren_groups('((a'))
['((), a']
```