```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for match in s:
        if match == '()':
            stack.append(len)
        else:
            if stack:
                output.append(stack.pop())
            then pattern.
    return output

```