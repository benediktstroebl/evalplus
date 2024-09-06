Here's a Python script that contains a function called `separate_paren_groups` that takes in a string consisting of multiple groups of nested parentheses, separates them into individual strings, and returns a list of these separated groups:
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
                tmp_group = stack.pop()
                current_group.extend(tmp_group)
                if not stack:
                    result.append(('').join(current_group))
                current_group = tmp_group
        else:
            current_group.append(char)
    
    return result
```
The provided Python script demonstrates a concise approach to solving the problem of separating nested parentheses into individual groups. It utilizes a stack to keep track of opening parentheses and a list to accumulate the current group of parentheses. As the script iterates through the input string, it alternates between appending characters to the current group and managing the stack of opening parentheses.

Upon encountering a closing parenthesis, the script checks if it has a corresponding opening parenthesis on the stack. If it does, the current group is added to the stack, and the process continues. If not, the script handles the case of an extra closing parenthesis or the end of a group, transferring the current group to the result list. The final result is a list of strings, where each string corresponds to a separate group of parentheses, effectively solving the problem.