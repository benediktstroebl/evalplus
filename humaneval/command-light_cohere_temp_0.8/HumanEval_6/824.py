```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for char in parenthes:
        if char == " ":
            if in_string:
                stack.append(len)
                in_string = False
        elif char == "(" and not in_string:
            in_string = True
            stack.append(1)
        elif char == ")" and in_string:
            in_string = False
            stack.pop()
        if len(stack) > 0:
                output.append(stack.pop()
   
            if in string and char != "(" and ")"):
                stack.append(0)
        elif in_string:
            in_string = False
    return output
```