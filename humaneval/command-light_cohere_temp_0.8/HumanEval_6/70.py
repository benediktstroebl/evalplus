```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                result.append(len)
                stack.append(0)
            else:
                stack.append(stack.pop()
   args, the problem is a valid string, this function parses the nested parentheses correctly.