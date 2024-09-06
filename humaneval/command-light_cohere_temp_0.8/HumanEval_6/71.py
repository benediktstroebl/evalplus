```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0
    i = 0
    output: List[int] = []
    while i < len(parenthes_string):
        char = parenthes_string[i]
        if char == "(" and opening_level == closing_level:
            closing_level += 1
        elif char == ")" and opening_level == closing_level:
            opening_level = closing_level + 1
        elif char == "(":
            stack.append(closing_level)
        else:
            stack.append(opening_level)
            opening_level = closing_level + 1
        i += 1
    return stack
```
This function `parse_nested_parens` takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. It uses a nested list to keep track of opening and closing parentheses levels. The function utilizes a while loop and a stack to keep track of the parenthesis levels.