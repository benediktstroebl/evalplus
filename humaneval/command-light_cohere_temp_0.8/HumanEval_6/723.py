Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    stack = []
    opening = 1
    closing = 1

    for char in parenthesis_string:
        if char == '(' and opening:
            stack.append(opening)
            opening = 0
        elif char == ')' and closing:
            if stack:
                stack.pop()
                closing
            if stack:
                closing = 0
                stack.append(opening)
                opening = 1
        elif char != '(' and closing:
            stack.append(closing)
            closing = 0
        elif char == '(' and closing:
            stack.append(closing)
            closing = 1
            opening = 0

    return stack
```
The function `parse_nested_parens` in this code accepts a string containing numerous parenthesis groups separated by spaces as input. The string is parsed and transformed into a stack of integers that reflect the order of opening and closing parenthesis by monitoring the opening and closing parentheses and keeping track of the stack. The integers in the stack are returned in the final answer.