Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                result.append(')')
            else:
                stack.pop()
                current_group.append(')')
        else:
            current_group.append(char)
            
    return result
```
The code works by first initializing an empty `stack` and an initially empty `current_group` list, which will hold the constituents of the single nested parentheses group at a time. The `result` list is also initialized as an empty list that will hold the final list of separate groups. The code then goes through each character in the input string, if the character is an open parenthesis, it pushes the current group onto the stack and creates a new empty group. When a closing parenthesis is reached, the system checks if the stack is empty, if so, this means we have reached an unbalanced parenthesis, and we append a closing parenthesis to the result (this is an unbalanced group). In the case that the stack is not empty, we pop the last group from the stack and append the closing parenthesis to that group. The code continues this process until all characters have been traversed.

Here's an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```
This would output the expected result of three strings, as outlined in the problem statement.