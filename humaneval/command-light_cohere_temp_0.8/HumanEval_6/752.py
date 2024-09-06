```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                output.append(stack.pop()..pop()
        a value the will.pop(stack)
        stack)
            stack.append(0)
    if char == ')':
                stack.append(1)
            else:
                if len(stack) == 0:
                    output.append(0)
                else:
                    output.append(stack.pop() +)
                    next  char is in ') )
                        stack.append(1)
            return output
```
The `parse_nested_parens` function is a self-contained function that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string.