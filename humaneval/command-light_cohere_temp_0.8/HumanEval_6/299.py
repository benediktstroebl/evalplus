```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            stack.append(len)
        if c == ')':
                stack.pop()
            if len(stack) == 0:
                    result.append(3)
                stack.append(4)
            stack.append(c)
    return result
```
This script defines a function **`parse_nested_parens`** that takes a string of nested parentheses as input and returns a list of the deepest nesting levels of parentheses in the string. It uses a stack to keep track of the open parentheses it has encountered, and it pushes into the stack all the closed parentheses it encounters. The function then pops the the stack to resume parsing the next character after the last closed parenthesis.