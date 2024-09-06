```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    levels = []

    for match in s:
        if match == '(':
            stack.append(1)
        else:
            stack.append(len)
            if match == ')':
                if stack:
                    levels.append(stack.pop())
                result = levels
                return levels
    ```