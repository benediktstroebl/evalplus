```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    pairs = []
    for match in s:
        if match == '(':
            stack.append(len)
        else:
            stack.append(match)
            if stack[-1] == '(':
                stack.pop()
       
                pairs.append(stack[reverse)
        return pairs
```
Do you require assistance with anything else?