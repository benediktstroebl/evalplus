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
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The provided Python script aims to tackle the issue of splitting a given string containing multiple groups of nested parentheses into separate, non-intersecting strings. To achieve this, it uses a stack mechanism to keep track of nested parentheses groups.

Here is an example of how you can call this function:
```python
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

The expected output for this input would be:
```
['()', '(())', '(()())']
```

This function serves as an illustrative example of how nested data structures like lists and stacks can be employed in Python to solve complex problems. It demonstrates the importance of careful tracking of opening/closing brackets and the proper usage of data structures to achieve the desired result.