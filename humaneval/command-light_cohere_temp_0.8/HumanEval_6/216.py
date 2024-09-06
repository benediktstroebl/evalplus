```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                opening_level, _ = stack.pop()
                opening_from_parens
                result.append(opening_level)
            else:
                stack.append(0)
        else:
                stack.append(char)
    return result
```  This function takes a string of nested parentheses separated by spaces as input and returns the deepest level of nesting of parentheses in the string. It uses a stack data structure to keep track of opening parentheses and appends the corresponding opening level to the result list when a closing parent is encountered.