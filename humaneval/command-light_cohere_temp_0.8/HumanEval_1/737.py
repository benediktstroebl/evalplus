```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Removes all spaces and splits the string by parentheses into a list of strings.
    Modified 2020.10 to ensure code test multiple groups of different types of parentheses.
    """ This very unbalanced way to identify and separate different types of parentheses
    """
    result = []
    stack = []
    for char in s:
        if char == ' ':
            stack.append(')')
       
        elif char == ')':
            result.append(stack.pop())
           
       
            stack,
            stack = []
        elif char == '(':
            stack.append(')')
        elif char == ')(':
            stack.append(')')
            else:
                stack.append(char)
    finally, result. process the entire string to return the output. 
```