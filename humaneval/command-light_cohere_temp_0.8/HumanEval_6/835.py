```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    # A nested list of parentheses is parsed and returned
    stack = [0]
    res = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
       if weadd:
                res.append(stack[-1])
                stack = [0]
    return res
# Tests are provided in the same script, right before the function
# Test 1: Output the deepest level of nesting of parentheses.
# Test 2: Output list with length 4
```