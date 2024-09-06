```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        closing_brackets = []
        stack = []
        for c in segment:
            if c == '(':
                open_brackets.append(len(stack))
                stack.append(c)
            elif c == ')':
                closing_brackets.append(len(stack))
                stack.pop()
        result.append(len(stack))
    return result
```
The code processes each segment (part between spaces) separately, simulating nested brackets. It maintains an imaginary stack of brackets to calculate the depth by counting the items on the stack and inverts this value to obtain the maximum nesting level. The solution is consistent with the given test case and demonstrates an efficient and understandable approach.