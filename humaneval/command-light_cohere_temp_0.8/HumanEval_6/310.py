```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    out_string = False
    start_string = True
    parentheses = []

    for char in s:
        if char == "(":
            if not in_string:
                stack.append(1)
            in_string = True
            start_string = False
        elif char == ")":
            if in_string:
                stack.append(1)
                in_string = False
            out_string = True
        elif start_string:
            if char == "(":
                stack.append(1)
            start_string = False
        elif char in "!)":
            if out_string:
                parentheses.append(stack.pop())
       
            return parentheses
   
    return parentheses
```
This function uses a stack data structure to track levels of nesting and a set of characters to identify when a closing parenthesis should be added to the stack. The function iterates through each character in the input string and adds the character to the stack if it is a opening parenthesis. If the character is a closing parenthesis, the function removes the character from the stack and adds the character to the output list. This process continues until all input string is empty or there are no more opening parenthesis.