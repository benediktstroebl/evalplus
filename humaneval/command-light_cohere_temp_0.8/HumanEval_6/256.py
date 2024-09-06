```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack or stack[-1] == 1:
                stack.pop()
            else:
                stack.append(3)
        else:
                stack.append(2)
    output.push(len(stack))
    return output
parentheses_str = """(()()) ((())) () ((())()())"""
print(parse_nested_parens(parentheses_str))
```