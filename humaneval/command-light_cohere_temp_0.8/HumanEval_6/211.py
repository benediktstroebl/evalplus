```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                output.append(len)
            stack.append(0)
        elif stack and stack[-1] > 1:
                output.append(stack.pop())
            stack.append(0)
   
    return output
``` 
This script defines a function **`parse_nested_parens`** that takes a string of nested parentheses and returns a list of the deepest level of nesting parentheses in the string. The function uses a **`stack`** to keep track of the nesting levels and the current character in the string. It uses a **`output`** list to keep track of the deepest level of nesting parentheses found so far.