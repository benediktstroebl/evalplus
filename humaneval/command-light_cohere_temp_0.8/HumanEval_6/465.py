```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for t in s:
        if t == '(':
            stack.append(1)
        elif t == ')':
            if len(stack) == 0:
                output.append(0)
            stack.append(0)
        else:
                stack.append(stack.pop()
   }
    stack.pop()
    many of the new, the number will be the deepest level of nesting in the input string.
``` 
Output:
```[3, 2, 1, 3]```