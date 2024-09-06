Here's the self-contained Python script with the function `parse_nested_parens` that solves the problem of identifying the deepest level of nesting for a given string of parentheses:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    in_brace = False
    for char in parentheses_string:
        if char == " ":
            stack.append(0)
            in_brace = True
        elif char == "(":
            if in_brace:
                stack[-1] += 1
            else:
                stack.append(1)
            in_brace = False
        elif char == ")":
            if in_brace:
                stack[-1] -= 1
            else:
                stack.append(0)
            in_brace = False
        elif char == "(":
            stack.append(1)
            in_brace = True
        elif char == ")":
            stack.pop()
            return stack
return stack
```
This function uses a stack data structure to keep track of the open parentheses. It iterates over the first character in the string, and keeps track of the level of nesting. The function returns a list of integers that represents the deepest level of nesting found in the string.