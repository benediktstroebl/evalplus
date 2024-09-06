```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0
    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            closing_level += 1
        else:
            stack.push(closing_level -  - opening_level)
            opening_level = 0
            closing_level = 0
    return stack
#
# Example usage:
test_parse_nested_parens("(((()()) ((())) ) ((()))()"))")
# [2, 3, 1, 3]
test_parse_nested_parens("((())())((())()())")
# [1, 2, 3]
test_parse_nested_parens("((()()()()()()()()()()()()()))")
# [4]
```