```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            stack.append(c)
   
        return output
```
Do you require any assistance with implementing other problems or writing code?