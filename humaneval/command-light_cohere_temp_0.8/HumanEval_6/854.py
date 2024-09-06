```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for char in s:
        if char == ' ':
            if in_string:
                stack.append(output.append(1))
                in_string = False
            continue
        elif in_string:
            in_string = False
            continue
        elif char == '(':
            in_string = True
        else:
            in_string = False
            stack.append(output.append(char))
    return output
```  This code defines a function `parse_nested_parens` that takes a string of nested parentheses and returns the deepest level of nesting for each group of parentheses in the string. It uses a stack to keep track of the current level of nesting and appends the deepest level to the stack when a new parenthesis is encountered. 
The code uses a combination of spaces and parentheses to create this behavior and returns the output from the stack.