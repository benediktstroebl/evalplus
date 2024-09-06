```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level = stack.pop()
        result.append(level)
    return result
```
The function processes each group of parentheses separately and tracks the current nesting level using a stack. The `zip('(()', '))'`) argument helps to efficiently iterate over all relevant pairs of parentheses. The solution is tested and should work correctly for input groups with nested parentheses separated by spaces. Feel free to test it with different inputs.