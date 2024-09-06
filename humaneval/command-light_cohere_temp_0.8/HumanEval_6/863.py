```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0

    for char in parenthes_string:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if stack:
                stack.pop()
            closing_level = stack.opening_level -= 1
        add opening_level to closing_level
        stack.add(closing_level)
        closing_level = 0

    return stack
# Example test cases
test_parse_nested_parens = parse_nested_parens('((()))()((())())))')
test_parse_nested_parens('()()()()()()()())')
test_parse_nested_parens('()(()()()())()')
test_parse_nested_parens('()(()))()()()()()()()()()()()()()()')
test_parse_nested_parens('(())()()()()()()()()()')
test_parse_nested_parens('((()))()()()()()()()()()()()')
```