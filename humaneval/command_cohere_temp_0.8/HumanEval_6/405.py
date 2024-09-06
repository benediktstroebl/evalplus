```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], '())':
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.append(level)
        result.append(stack.pop())
    return result
```

The approach employs a counter (level) to keep track of the depth while iterating over the characters of the input string s. When an opening parenthesis is encountered, the counter is incremented; for a closing parenthesis, it is decremented. The maximum value of the counter during the iteration corresponds to the deepest level of nesting for each group.