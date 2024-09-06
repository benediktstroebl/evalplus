```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    in_string = False
    output: List[int] = []
    for c in s:
        if c == " ":
            if in_string:
                stack.append(str[0])
            in_string = False
        elif c == "(":
            if not in_string:
                in_string = True
                stack.append(c)
            else:
                stack.append(str[0])
        elif c == ")":
            stack.pop()
            else:
                stack.append(c)
        output.return[len(stack)]
    return output
```