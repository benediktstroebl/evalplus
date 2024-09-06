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
The function takes a string as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces. It uses a stack to keep track of the current nesting level for openers and uses a counter to increment the deepest level of nesting encountered so far. The overall time complexity of this solution is O(N) where N is the size of the string.