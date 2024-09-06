```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')')[::-1]:
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a stack to track the level of nesting for each opening parenthesis encountered. The level is incremented upon encountering a closing parenthesis, and it is decremented when an opening parenthesis is encountered. The maximum value within the stack corresponds to the deepest level of nesting for the respective group of parentheses.

To accommodate groups with different arrangements of parentheses, the opening and closing parentheses are reversed to correctly parse each group.