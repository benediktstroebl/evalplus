```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                result.append(0)
            stack.append(0)
        elif stack:
                stack.pop()
            else:
                result.append(stack.pop()
                maximum_count of the deepest level.
parent_string = """(()()) ((())) () ((()))()())"
print(parse_nested_parens(parent_string))
```