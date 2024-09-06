Here's the code:
```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack: List[int] = []
    for match in parenthes.match=(match.group(0): Group),:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if len(stack) == 0:
                stack.append(0)
            else:
                stack.append(len[-1])
            else:
                stack.append(2)
    else:
                stack.append(3)
    return stack
```

This function takes a string of nested parentheses and returns a list of its deepest nested parentheses.  The test cases are also provided, which should successfully test the function.