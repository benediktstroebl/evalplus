```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    output = []
    for c in s:
        if c == "(" and not in_string:
            in_string = True
        stack.append(1)
        if c == ")" and in_string:
            in_string = False
        if c == ")" and stack:
            stack.pop()
            if c == "(" and stack:
            output.append(3)
    return output
```
This function, parse_nested_parens, takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses found. The function uses a stack data structure to keep track of the deepest level of parentheses encountered so far.  It string is enclosed in parentheses and also within any other parentheses that are being processed.