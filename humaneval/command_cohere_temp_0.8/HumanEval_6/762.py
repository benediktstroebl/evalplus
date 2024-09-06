```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        stack = []
        depth = 0
        for char in chunk:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                if not stack or stack[-1] < depth:
                    result.append(depth)
                depth -= 1
                stack.pop()
        if not stack or stack[-1] < depth:
            result.append(depth)
    return result
```

The code processes each chunk (parentheses group) separately and solves the problem in a recursive manner. The `depth` variable is used to keep track of the current depth of nesting, and the `stack` list helps to manage recursive grouping. The output is a list where each element corresponds to the deepest level of nesting amongst the corresponding parentheses group.