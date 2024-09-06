```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Split a string of parenthesis into a list of separate groups.
    :return: list of separate group strings
    """
    list_output = []
    Stack = []
    for char in s:
        if char == '(': Stack.push(char)
        elif char == ')': 
            if Stack:
                list_output.append(Stack.pop())
               Stack.push(char)
   
    else: Stack.push(char)
    return list_output
``` 
This function, `separate_paren_groups`, takes a string as input and returns a list of separate parenthesis groups. It utilizes a method `pop` and `pop` to create a stack of open parenthesis, and then uses `push` to add close parenthesis to the stack.