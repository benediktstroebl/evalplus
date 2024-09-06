```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    in_string = False
    result = []
    for c in s:
        if in_string:
            if c == '(':
                stack.append(1)
                in_string = False
            continue
        elif c == ')':
            if len(stack) == 0:
                in_string = False
            elif stack[-1] == 1:
                stack.pop()
                in_string = False
                continue
            else:
                stack.append(3)
                in_string = False
            continue
        else:
            in_string = True
    return result
# Example usage
input_string = '(()()) ((())) () ((())()())'
result = parse_nested_parens(input_string)
print(result)
```