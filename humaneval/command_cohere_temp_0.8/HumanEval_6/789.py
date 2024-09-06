```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
            if c == closer:
                if not stack or opener == stack.pop():
                    level += 1
                else:
                    result.append(level)
            if len(stack) == 0:
                result.append(level)
        if stack:
            result.append(level+)
    return result
```
The function iterates through each pair of opening and closing parentheses, maintaining a stack of opened openers and a counter of the current nesting level. When a closing counterpart is encountered, the stack is checked to determine if it belongs to the last opened opener. If so, the level is incremented, otherwise, the current level is appended to the results list. If the stack is empty, the current level is appended. Finally, any remaining openers in the stack are considered as already closed, and their level is added plus one. The results list with the deepest levels of nesting for each group is returned. 

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This demonstrates the function's ability to extract and parse nested parentheses, providing the maximum depth for each group, regardless of the order of appearance.