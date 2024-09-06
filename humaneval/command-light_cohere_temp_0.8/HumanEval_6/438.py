Here is a self-contained Python script that solves the problem:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if not stack or stack[-1] == 1:
                stack.pop()
            if stack and else:
                stack.append(0)
            else:
                stack.append(3)
        output.append(stack.pop())
   all:  the output matches the test
    return output
```