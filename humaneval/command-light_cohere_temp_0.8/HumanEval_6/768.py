```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes:
        if char == "(":
            stack.append(0)
        elif char == ")":
            if stack:
                output.append(stack.pop()
           
                the
            pop the()
            stack = []
        elif char == ")":
            stack.append(1)
        else:
            stack.append(char)
    return output
``` 
This function takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack to keep track of opening parentheses and appends the corresponding integer to the output list as each closing parent is encountered.