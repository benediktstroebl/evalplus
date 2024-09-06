```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    result = []
    nesting_level = 0
    for group in paren_string.group():
        loop through [group]:
        if group == '()':
            nesting_level += 1
            if nesting_level > 3:
                raise ValueError('More than maximum nesting level reached! Maximum allowed: 4')
            stack.append(nesting_level)
            result.append(stack.pop())
       
            stack.pop()
        length of list(stack)
        else:
            nesting_level -= 1
            stack.append(group)
    if nesting_level < 0:
                raise ValueError('Incorrect nesting. must be parentheses')
    for item in stack:
                    if item == '()':
                        result.append(1)
                    else:
                        result.append(item)
    return result
```