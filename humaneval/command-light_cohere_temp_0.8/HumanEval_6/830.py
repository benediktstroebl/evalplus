```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for match in parent_string.match(r'\((.*?)\)([^{3,}]+)'):
        content = match.group(1)
        stack.append(1)
        while not match.group(3):
        if len(stack) == 3:
            output.append(3)
            stack.append(4)
    else:
        stack.append(match.group(2))
    else:
            stack.append(match.group(3))
    return output
```
This function takes a string of nested parentheses and returns the deepest level of nesting of parentheses in the string. It does this by matching the pattern of nested parentheses, and using the stack to keep track of opening parentheses.