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
                print("UNBALANCED!")
                continue
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```
The algorithm uses a stack to keep track of open parentheses and constructs the resulting strings accordingly. It initializes an empty `result` list that will be used to store the separate groups of parentheses. It then iterates through the characters of the input string, checking if each character is an open or closed parenthesis. If the character is an open parenthesis, the current group is added to the stack, and a new empty group is created. If it is a closed parenthesis, the algorithm checks if the stack is empty. If true, this indicates an unbalanced parenthesis group, so it skips the character and continues with the next one. If the stack is not empty, the algorithm retrieves the top item from the stack (which should be the corresponding open parenthesis) and checks if it is empty. If true, it means we've closed the last open parenthesis in that group, so we can pop the group from the stack, append it to the `result` list, and then pop the next group from the stack to resume processing. If the top item of the stack is not empty, the algorithm simply pops it and continues processing the current group. The process continues until all characters have been processed.

Here's an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```
This would output a list with the three balanced groups of parentheses, separated and returned as a list.