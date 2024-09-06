```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    nesting_levels = []
    for char in parenthes_string:
        if char == ')':
            if stack:
                nesting_levels.append(lenum(stack))
                stack.pop()
        stack.
        elif char == '(':
            stack.append(1)
        nesting_levels.append(0)
    stack.
    return nesting_levels
```

This function, `parse_nested_parens`, takes a string of nested parentheses as input and returns a list of nesting levels. It uses a nested list to simulate the nesting of parentheses and numbers indicate the depth of the nesting.

The function works by iterating over each character in the input string. When a '(' is encountered, a new element is pushed onto the stack, and the nesting level is set to 0. When an ')' is encountered, the function checks if there is a non-empty stack. If so, the function pops the last element from the stack, adds the un-papped element to the list of nesting levels, and resets the stack to an empty list.