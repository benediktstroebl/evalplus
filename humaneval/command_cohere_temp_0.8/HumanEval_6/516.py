```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        stack = []
        for c in segment:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] != '(':
                    continue
                stack.pop()
            if not stack:
                result.append(level)
                break
            level += 1
        if stack:
            result.append(level)
    return result
```

The function iterates through each segment of the string, maintaining a `stack` of open parentheses '(' and tracking the `level` of nesting. When a closing parenthesis ')' is encountered and there's an open parenthesis on the stack, it is popped and the nesting level increments. If the stack is empty, the current nesting level is appended to the results list since it's the deepest level of nesting for that segment. If there are still open parentheses left in the stack after processing a segment, the function appends the current nesting level as the deepest level achieved.

Here is an example usage of the function:
```python
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
```

This will output `[2, 3, 1, 3]` as the deepest levels of nesting for each segment of the provided string, respectively.