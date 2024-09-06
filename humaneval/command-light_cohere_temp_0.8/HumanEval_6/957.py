```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function is designed to parse a string containing nested parentheses. It returns a specified levels of nesting as a list of integers.
    >>> parse_nested_parens('(()()) ((())) () ((()))()')
    [2, 3, 1, 3]
    """
    stack = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                return []
            stack.pop()
       
   
            if len(stack) > 0:
                stack.append(stack.pop()
   
            else:
                stack.append(0)
    return stack
    ``` 
This function employs a stack data structure to manage the opening and closing parentheses. It iterates through characters of the input string, starting with '(' and ')'. It adds '(' to the stack when it encounters an open parent, and adds the corresponding closing parent to the stack when it encounters a ')'. It returns the final stack, which contains the nesting level of each group of parentheses in the string.