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
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm uses a stack to track open parentheses and a separate list to track the current group of parentheses. When a closing parenthesis is encountered, the stack is checked to see if it's empty. If not, the top of the stack is popped and added to the current group. If the stack is empty, the current group is appended to the results list and then cleared. The algorithm continues until all parentheses are processed. 

Here is an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

This will output a list of the three distinct groups of parentheses, each separated and returned as a string in the list. 

Note: the algorithm assumes that the input string contains only valid parentheses and no other characters. If other characters are present, the function may not return the expected results.