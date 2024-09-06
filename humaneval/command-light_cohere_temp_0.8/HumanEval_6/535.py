```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nesting = 0
    for char in s:
        if char == "(":
            nesting += 1
        elif char == ")":
            nesting -= 1
        elif nesting == 0:
            stack.append(nesting)
    return stack
```

This code defines a recursive function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest nesting levels. The function works by maintaining a stack of open parentheses and counting the nesting level of each closed pair. It starts with the `nesting` set to 0 and iterates over each character in the input string. 

The function adds the nesting level to the stack when an open parenthesis is encountered and subtracts 1 from it when a close parenthesis is encountered. This ensures that the maximum nesting level is limited to the number of open parentheses minus 1. 

When the function has encountered the end of no nesting (i.e. all stack is due array empty list), the result will be the final nesting level. 

This is a self-contained function that takes a string of nested parentheses and returns the deepest level of nesting.