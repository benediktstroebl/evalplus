```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    nesting = 0
    for c in parent_string:
        if c == '(':
            nesting += 1
        else:
            nesting -= 1
        if nesting == 0:
            stack.append(nesting)
    return stack
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest nesting levels found in that string. The function uses a stack to keep track of the nesting levels, and it iterates through the input string, checking each character to see if it's a opening parenthesis ('('). If it is, the nesting level is incremented, if it's a closing parenthesis, the nesting level is decremented. If the nesting level reaches 0, the closing parenthesis is added to the stack. The function returns the list of the deepest nesting levels found.