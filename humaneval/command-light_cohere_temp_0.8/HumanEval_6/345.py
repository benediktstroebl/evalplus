```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nesting_levels = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
            nesting_levels.append(1)
       
        elif char == ")":
            if len(stack) == 0:
                nesting_levels.append(0)
            stack.remove()
            stack
           
        else:
                nesting_levels.append(nesting_levels[-1] + 1)
            stack.append(i)

    return nesting_levels
```
This Python script defines a function named parse_nested_parens that takes a string containing multiple groups of nested parentheses separated by spaces as input. The function uses a typing convention to define a string s representing the input and returns a list of nesting levels. 

The function operates by maintaining a stack of parenthesis indices and a list of current nesting levels. When a "(" character is encountered, the index is added to the stack, and the current nesting level is incremented. When a ")" character is encountered, the function checks if the stack is empty. If it is empty, the nesting level is set to 0. If the stack is not empty, the current nesting level is the sum of the last nesting level and the current level, and the stack is popped to reset the stack for the next group of parentheses.