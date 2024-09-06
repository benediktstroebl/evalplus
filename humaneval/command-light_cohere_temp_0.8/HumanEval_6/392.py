```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nest_level = 0
    output = []
    for c in s:
        if c == '(':
            nest_level += 1
            stack.append(nest_level)
        elif c == ')':
            nest_level -= 1
            if nest_level == -1:
                output.append(stack.pop()
                stack)
        flatten list, return output
``` 
This function parses a string with nested parentheses and returns the deepest level of nesting of parentheses.