```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for t in s:
        if t == '(':
            stack.append(t)
        else:
            if not stack or t == ')':
                output.append(stack.pop()
                out list of test.  # it could. (^)\)()
        stack.pop()
   .append(t)
stack.delete
        stack = []
    return output
```  This script defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of their deepest nesting levels of parentheses. The `type` hints in the function help to convey the expected input and output types.