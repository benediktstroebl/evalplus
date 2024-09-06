```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    for c in parent_string:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                stack.pop()
            else:
                stack.append(3)
   return thestack, reversed and converted to integers for easier comparison.
parent_str = '(()()) ((())) () ((()))()'
nested_parens = parse_nested_parens(parent_str)
print(nested_parens)
``` 
This function, `parse_nested_parens`, takes a string as input and returns a list of integers that represents the deepest level of nesting of parentheses in the string. 

This function uses a stack data structure to keep track of open parentheses and their nesting levels. 
The function first iterates over the characters in the string. If a character is '(', it is added to the stack. If the character is ')', it checks if the stack is empty or the topmost open parent is 1. If it is empty, the current open parent is closed. If it is not empty and the topmost open parent is not 1, it is closed and the next open parent is added to the stack.