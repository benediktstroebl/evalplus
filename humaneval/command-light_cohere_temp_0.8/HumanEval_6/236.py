```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == ')':  # match closing parenthesis
            if not in stack: stack.pop()  # add to output
            if char == '(' and stack: stack.pop()
       
            else: stack.push(ord(char))
    return output
```