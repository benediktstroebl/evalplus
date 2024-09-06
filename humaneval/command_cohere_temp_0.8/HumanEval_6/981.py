```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        levels = []
        for char in s:
            if char == opener:
                stack.append(stack[-1] + 1)
            elif char == closer:
                stack.pop()
                levels.append(stack[-1])
        result.append(max(levels))
    return result
```
The function takes a string as input and returns a list of deepest levels of nesting of parentheses in each group. It uses a stack to keep track of the current nesting level for openers and iterates through the characters in the string, increasing and decreasing the stack accordingly. The maximum nesting level for each group is retained in the `result` list.