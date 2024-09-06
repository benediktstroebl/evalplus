Here is a self-contained Python script with a function that solves the problem of parsing and identifying nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_group = False
    output = []
    for char in s:
        if char == '(':
            if in_group:
                stack.append(len)
                in_group = True
            output.append(1)
        else:
            in_group = True
        elif char == ')':
            if not in_group:
                stack.pop()
                in_group = False
            output.append(len)
        else:
            in_group = False
        else:
            continue
    return output
```
The code uses a stack data structure to manage the opening and closing parentheses as the string is being parsed. It iterates through string character by character, making decisions about whether to add to the stack, or to the current group of parentheses, and pushes the appropriate values onto the stack. The loop continues until there are no more parentheses left in the string. The function returns the list of the top-level nesting of parentheses in the string.