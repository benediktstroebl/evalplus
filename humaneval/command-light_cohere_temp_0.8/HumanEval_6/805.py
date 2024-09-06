```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    openings = closures = []
    in_stack = False
    for char in parentheses_string:
        if char == "(":
            if not in_stack:
                stack.append(1)
                in_stack = True
        elif char == ")":
            if in_stack:
                stack.pop()
                in_stack = False
        else:
            openings.append(char)
        elif char == "(" and in_stack:
            stack.append(0)
            closures.append(0)
            in_stack = True
        else:
            if in_stack:
                stack.append(int(char))
                closures[len(stack) - 1] = closures[len(stack) - 2] + 1
                in_stack = False
    if not in_stack:
        stack.pop()
        in_stack = False
    return [stack[-1] for stack in stack]
# tests
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()')') == [2, 3, 1, 3]
test_parse_nested_parens()
``` 
The code defines a function **parse_nested_parens** that takes a string of nested parentheses and returns a list of their depths. The function uses a stack to keep track of opening parentheses and their closures. It uses a to maintain the current state of parentheses and their opening and closing characters.