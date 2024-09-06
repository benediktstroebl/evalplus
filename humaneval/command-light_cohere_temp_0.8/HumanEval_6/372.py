```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                raise ValueError("Unexpected character ')'.")
            else:
                output.append(stack.pop()
       pop.
        stack.append(char)
   _to_str(char))
        stack.pop()
    pop()

    return output
```

This function, parse_nested_parens, takes a string of nested parentheses as input and returns a list of the deepest levels of nesting of parentheses in the string. It uses a stack to keep track of open parentheses and populates/appends to the output list as the parentheses are closed.  The stack is then popped from and converted into a string to match the original input. The output list contains the maximum nesting level found.