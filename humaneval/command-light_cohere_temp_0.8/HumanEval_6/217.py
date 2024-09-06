```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False  # flag to track if we are inside a string
    opening_brack = ""  # to track the last opening bracket encountered
    closing_brack = ""  # to track the last closing bracket encountered

    for char in s:
        if char == " ":
            if in_string:
                stack.append(int(closing_brack))
                closing_brack = ""
            in_string = False
        elif char == "(" and not in_string:
            in_string = True
            opening_brack = char
        elif char == ")" and in_string:
            in_string = False
            stack.append(int(opening_brack))
            closing_brack = char
        elif char == "(":
            stack.append(int(opening_brack))
        elif char == ")":
            stack.appendleft stack.pop()  # stack
        final values
    return stack
```